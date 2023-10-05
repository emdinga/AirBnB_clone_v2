#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import env, local, run, lcd, cd
from datetime import datetime
from os.path import exists

# Environment configuration
env.hosts = ['18.214.88.155', '100.25.150.236']
env.user = 'ubuntu'

def do_clean(number=0):
    """
    Deletes out-of-date archives
    """
    number = int(number)
    if number < 0:
        return

    # Local clean (delete archives)
    local_archives = local("ls -t versions", capture=True).split()
    archives_to_delete = local_archives[number:]
    for archive in archives_to_delete:
        local("rm -f versions/{}".format(archive))

    # Remote clean (delete archives)
    releases_path = "/data/web_static/releases"
    releases = run("ls -t {}".format(releases_path)).split()
    archives_to_delete = releases[number:]
    for archive in archives_to_delete:
        run("rm -rf {}/{}".format(releases_path, archive))

