#!/usr/bin/python3

"""Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from datetime import datetime
from os import path


env.hosts = ['54.234.60.152', '54.146.94.81']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""

    try:
        if not (path.exists(archive_path)):
            return False

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # create folder
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/\
                web_static_{}/'.format(timestamp))

        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/\
                web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # Delete the archive from the web server
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
                /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove extra web_static folder
        run('sudo rm -rf /data/web_static/releases/\
                web_static_{}/web_static'
            .format(timestamp))

        # Delete the symbolic link /data/web_static/current fromweb server
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current linked
        run('sudo ln -s /data/web_static/releases/\
                web_static_{}/ /data/web_static/current'
            .format(timestamp))

    except Exception as e:
        return False

    # return True on success
    return True
