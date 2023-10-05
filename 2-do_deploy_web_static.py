#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers using do_deploy.
"""
from fabric.api import *
from os import path

env.hosts = ['18.214.88.155', '100.25.150.236']
env.user = 'ubuntu'
env.key_filename = '~/id_rsa'

def do_deploy(archive_path):
    """ Distribute an archive to your web servers """
    if not path.exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    dest_folder = "/data/web_static/releases/{}".format(file_name.split('.')[0])

    try:
        put(archive_path, '/tmp/')
        run("mkdir -p {}".format(dest_folder))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest_folder))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(dest_folder, dest_folder))
        run("rm -rf {}/web_static".format(dest_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_folder))
        return True
    except Exception:
        return False

