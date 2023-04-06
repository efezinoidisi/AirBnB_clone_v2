#!/usr/bin/python3
"""This module contains the Fabric script do_pack which generates a .tgz
archive from the contents of the web_static folder of this repository"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """generates a .tgz archive from the contents of the web_static folder"""
    current_date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(current_date)
    local('mkdir -p versions')
    result = local('tar -cvzf {} ./web_static'.format(filename))
    if result.return_code == 0:
        return filename
    else:
        return None
