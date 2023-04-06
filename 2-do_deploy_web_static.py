#!/usr/bin/python3
"""This module contains the Fabric script do_deploy that distributes an
archive to a web server"""

from fabric.api import run, put, env, local
from os import path
from datetime import datetime

env.use_ssh_config = True
env.hosts = ['134559-web-02', '134559-web-01']


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


def do_deploy(archive_path):
    """upload an archieve to server"""
    if not path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
    filename = archive_path.split('/')[1]
    filepath = "/tmp/" + filename
    name = filename.split('.')[0]
    des = '/data/web_static/releases/' + name
    run('mkdir {}'.format(des))
    run('tar -xvzf {} -C {}/'.format(filepath, des))
    run('rm {}'.format(filepath))
    run('rm -rf /data/web_static/current')
    first = 'mv /data/web_static/releases/{}/web_static/*'.format(name)
    run('{} /data/web_static/releases/{}/'.format(first, name, name))
    run('ln -s {}/ /data/web_static/current'.format(des))
    return True
