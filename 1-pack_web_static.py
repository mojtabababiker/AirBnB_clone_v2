#!/usr/bin/python3
""" Fabric script that pack and prepairs the static contents to be uploaded """

from fabric.api import *


env.hosts = ['18.204.3.225', '54.146.86.208']


def do_pack():
    """ Pack the contect of AirBnB static ino .tar """
    local("mkdir versions")
    name = local("date +%-Y%m%d%H%m%s", capture=True)
    result = local(f"tar -cvzf versions/web_static_{name}.tgz web_static",
                   capture=True)

    if result.failed:
        return None
    return "versoins/web_static_{name}.tgz"
