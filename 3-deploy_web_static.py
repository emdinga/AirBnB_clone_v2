#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers using do_pack and do_deploy.
"""
from fabric.api import local, env, run, put
from datetime import datetime
import os

env.hosts = ['18.214.88.155', '100.25.150.236']
env.user = 'ubuntu'
env.key_filename = '~/id_rsa'

def do_pack():
    """ Create a compressed archive from web_static folder """
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
        timestr = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_file = "versions/web_static_{}.tgz".format(timestr)
        local("tar -cvzf {} web_static".format(archive_file))
        return archive_file
    except Exception:
        return None

def do_deploy(archive_path):
    """ Distribute an archive to your web servers """
    if not os.path.exists(archive_path):
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

def deploy():
    """ Deploy the web_static content to your web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)

