#!/usr/bin/python3
"""
A fabfile to prepare the static file for deploying
"""
from fabric.api import *
from datetime import datetime
import os
import os.path


env.user = 'ubuntu'
env.hosts = ['54.84.73.143', '35.175.102.250']


def do_pack():
    """
    function which generates a .tgz archive from the contents
    of web-static in order to prepare it to be pushed to the
    server
    """
    date = datetime.now()
    name = date.strftime('%Y%m%d%H%M%S')

    if not os.path.isdir('versions'):
        os.mkdir('versions')

    result = local("tar -cvzf versions/web_static_{}.tgz web_static".format(
        name))

    if result.failed:
        return None

    size = os.path.getsize("versions/web_static_{}.tgz".format(name))
    print("web_static packed: versions/web_static_{}.tgz -> {}Bytes".format(
        name, size))

    return "versions/web_static_{}.tgz".format(name)


def do_deploy(archive_path):
    """
    push and uncompress the archive file in the `archive_path` to the server/s
    """
    if archive_path is None or not os.path.isfile(archive_path):
        return False
    try:
        result = put(local_path=archive_path, remote_path='/tmp/')
        name = os.path.basename(archive_path).split('.')[0]

        result = run(f"mkdir -p /data/web_static/releases/{name}/")
        result = run(f"tar -xzf /tmp/{name}.tgz" +
                     f" -C /data/web_static/releases/{name}/")
        result = run(f"cp -rf /data/web_static/releases/{name}/web_static/*" +
                     f"  /data/web_static/releases/{name}/")
        result = run(f"rm -rf /data/web_static/releases/{name}/web_static")
        result = run(f"rm -rf /tmp/{name}.tgz")
        result = run("rm -rf /data/web_static/current")
        result = run(f"ln -s /data/web_static/releases/{name}/" +
                     "  /data/web_static/current")
        # print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """
    handle the deploy proccess from the start to fully deploying
    statics into server/s
    """
    ar_path = do_pack()
    if not ar_path:
        return False

    return do_deploy(ar_path)
