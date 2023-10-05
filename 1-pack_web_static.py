#!/usr/bin/python3
"""
Fabric script that generates a .tgz
"""
from fabric.api import local
import tarfile
import os.path
import re
from datetime import datetime


def do_pack():
    """distributes an archive to your web servers
    """
    target = local("mkdir -p versions")
