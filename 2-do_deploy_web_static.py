#!/usr/bin/python3
""" Fabric script that pack and prepairs the static contents to be uploaded """

from fabric.api import *
import os
import os.path


env.hosts = ['18.204.3.225', '54.146.86.208']


def do_pack():
    """
    Pack the contect of AirBnB static ino .tar
    """
    if not os.path.isdir("./versions"):
        os.mkdir("./versions")
    name = local("date +%Y%m%d%H%m%S", capture=True)
    result = local(f"tar -cvzf versions/web_static_{name}.tgz web_static",
                   capture=True)

    if result.failed:
        return None
    return "versoins/web_static_{name}.tgz"


def do_deploy(archive_path):
    """ Distrubute an archive to the web server """
    try:
        if '/' in archive_path:
            archive_rel_path = archive_path.split('/')[-1]
        name = archive_rel_path.split('.')[0]
        tar_path = "/data/web_static/releases/{name}"
        put(local_path=archive_path, remote_path="/temp/")
        run(f"mkdir -p {tar_path}")  # create the new version static file
        # uncompress the archive file
        run(f"tar -xzf /temp/{archive_path} -C {tar_path}")
        # remove the archive file from /temp
        run(f"rm -f /temp/{archive_path}")
        # move all the statice from the web_static to the new release
        run(f"mv {tar_path}/web_static/* {tar_path}/")
        # remove the empty web_static directory
        run(f"rm -fr {tar_path}/web_static")
        # Delete the sympolic link and recreate it to link the new releas
        run(f"rm -f /data/web_static/current")
        run(f"ln -s {tar_path} /data/web_static/current")

    except Exception:
        return False

    return True
