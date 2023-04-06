#!/usr/bin/python3
"""This module contains the fabric script do_pack which generates a .tgz
archive from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    cd = datetime.now()  # current date varaible
    one = f'versions/web_static_{cd.year}{cd.month:02d}{cd.day:02d}'
    two = f'{cd.hour:02d}{cd.minute:02d}{cd.second:02d}.tgz'
    filename = one + two
    print(filename)
    local('mkdir -p versions')
    local(f'tar -cvzf {filename} ./web_static')
    return filename
