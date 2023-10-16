#!/usr/bin/python3
"""
Compress before sending.
"""
from fabric.api import local, env
from datetime import datetime

env.hosts = ['54.162.34.11', '100.25.140.43']


def do_pack():
    """
    Compress a folder to .tgz archive.
    """
    date = datetime.utcnow()
    path = "versions/web_static_{}.tgz".format(
        datetime.strftime(date, "%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static".format(path)).failed:
        return None
    return path
