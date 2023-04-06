#!/usr/bin/python3
"""This module contains the Fabric script do_pack which generates a .tgz archive from the contents of the web_static folder of this repository"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "web_static_{}.tgz".format(current_date)
    local('mkdir -p versions')
    local('tar -cvzf {} ./web_static'.format(filename))
    return filename
