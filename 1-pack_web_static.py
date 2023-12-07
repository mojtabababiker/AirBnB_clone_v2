#!/usr/bin/python3
""" Fabric script that pack and prepairs the static contents to be uploaded """


from fabric.api import *
import os
import os.path


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
