#!/usr/bin/python3

"""Fabric script that distributes an archive to your web servers,
using the function do_deploy
"""
from fabric.api import *
from os import path


env.hosts = ['54.234.60.152', '54.146.94.81']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""

    try:
        if not path.exists(archive_path):
            return False

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract timestamp from archive path
        timestamp = path.splitext(path.basename(archive_path))[0][-14:]

        # Create directory for the release
        run('mkdir -p /data/web_static/releases/web_static_{}/'.format(timestamp))

        # Uncompress archive and delete .tgz
        run('tar -xzf /tmp/{}.tgz -C /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # Delete the archive from the web server
        run('rm /tmp/{}.tgz'.format(timestamp))

        # Move contents from /web_static/ to timestamped folder
        run('mv /data/web_static/releases/web_static_{}/web_static/* '
            '/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # Remove extra web_static folder
        run('rm -rf /data/web_static/releases/web_static_{}/web_static'
            .format(timestamp))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s /data/web_static/releases/web_static_{}/ /data/\
                web_static/current'
            .format(timestamp))

    except Exception as e:
        print("Error:", e)
        return False

    return True
