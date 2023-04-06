#!/usr/bin/python3
"""This module contains the Fabric script do_deploy that distributes an
archive to a web server"""

from fabric.api import run, put, env
from os import path


env.use_ssh_config = True
env.hosts = ['134559-web-02', '134559-web-01']
def do_deploy(archive_path):
	"""upload an archieve to server"""
	if not path.exists(archive_path):
		return False
	put(archive_path, "/tmp/")
	filename = archive_path.split('/')[1]
	filepath = "/tmp/" + filename
	no = filename.split('.')[0]
	des = '/data/web_static/releases/' + no
	run('mkdir {}'.format(des))
	run('tar -xvzf {} -C {}/'.format(filepath, des))
	run('rm {}'.format(filepath))
	run('rm /data/web_static/current')
	run('ln -s {} /data/web_static/current'.format(des)
	)
	return True
