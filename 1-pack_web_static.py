#!/usr/bin/python3
"""
This module contains the fabric script do_pack
"""
from fabric.api import local, task
from datetime import datetime
from pathlib import Path


@task
def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    """
    cd = datetime.now()  # current date varaible
    one = f'versions/web_static_{cd.year}{cd.month:02d}{cd.day:02d}'
    two = f'{cd.hour:02d}{cd.minute:02d}{cd.second:02d}.tgz'
    filename = one + two
    print(filename)
    path = Path("./versions")
    if not path.exists():
        local('mkdir versions')
    local(f'tar -cvzf {filename} ./web_static')
    return filename
