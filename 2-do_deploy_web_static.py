#!/usr/bin/python3
"""
Deploy archive!
"""
from fabric.api import put, run, env
from os.path import exists

env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'
env.hosts = ['54.162.34.11', '100.25.140.43']


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
