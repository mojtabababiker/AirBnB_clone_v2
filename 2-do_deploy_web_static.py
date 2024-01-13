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
    result = put(local_path=archive_path, remote_path='/tmp/')
    if result.failed:
        return False
    name = os.path.basename(archive_path).split('.')[0]

    result = run("mkdir -p /data/web_static/releases/{}/".format(name))
    if result.failed:
        return False
    result = run("tar -xzf /tmp/{}.tgz".format(name) +
                 " -C /data/web_static/releases/{}/".format(name))
    if result.failed:
        return False

    result = run("cp -rf /data/web_static/releases/{}/web_static/*".format(
        name) + "  /data/web_static/releases/{}/".format(name))
    if result.failed:
        return False

    result = run("rm -rf /data/web_static/releases/{}/web_static".format(name))
    if result.failed:
        return False

    result = run("rm -rf /tmp/{}.tgz".format(name))
    if result.failed:
        return False

    result = run("rm -rf /data/web_static/current")
    if result.failed:
        return False

    result = run("ln -s /data/web_static/releases/{}/".format(name) +
                 "  /data/web_static/current")
    if result.failed:
        return False

    print("New version deployed!")
    return True
