#!/usr/bin/python3
"""
Do complete deploy of the web static
"""
from datetime import datetime
from os.path import exists
from fabric.api import put, run, env, local


env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'
env.hosts = ["35.229.34.27", "35.237.166.174"]


def do_pack():
    """
    Compress a folder to .tgz archive.
    """
    date = datetime.utcnow()
    path = "versions/web_static_{}.tgz".format(
        datetime.strftime(date, "%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    if local("tar -cvzf {} web_static".format(path)).failed:
        return
    return path


def do_deploy(archive_path):
    """
    distributes an archive to the web servers
    """
    if exists(archive_path) is False:
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        arch_name_no_extension = archive_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, arch_name_no_extension))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_name,
            path, arch_name_no_extension))
        run('rm /tmp/{}'.format(archive_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path,
            arch_name_no_extension))
        run('rm -rf {}{}/web_static'.format(path, arch_name_no_extension))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path,
            arch_name_no_extension))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to web servers
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
