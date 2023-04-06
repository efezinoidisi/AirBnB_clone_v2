#!/usr/bin/python3
"""This module contains the Fabric script do_deploy that distributes an
archive to a web server"""

from fabric.api import run, put, env
from os import path


env.use_ssh_config = True
env.hosts = ['one']
def do_deploy(archive_path):
    """generates a .tgz archive from the contents of the web_static folder"""
    if not path.exists(archive_path):
        return False
    put(archive_path, "/tmp/")
