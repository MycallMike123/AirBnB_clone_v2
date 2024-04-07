#!/usr/bin/python3

"""Fabric script that creates and distributes an archive to your web servers,
using the function deploy
"""
from fabric.api import *
import os.path
from datetime import datetime

env.hosts = ['54.234.60.152', '54.146.94.81']


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder"""

    date_time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_time.year,
                                                         date_time.month,
                                                         date_time.day,
                                                         date_time.hour,
                                                         date_time.minute,
                                                         date_time.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None

    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to the web server"""

    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    _nam = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/".
           format(_nam)).failed is True:
        return False

    if run("mkdir -p /data/web_static/releases/{}/".
           format(_nam)).failed is True:
        return False

    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(file, _nam)).failed is True:
        return False

    if run("rm /tmp/{}".format(file)).failed is True:
        return False

    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(_nam, _nam)).failed is True:
        return False

    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(_nam)).failed is True:
        return False

    if run("rm -rf /data/web_static/current").failed is True:
        return False

    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(_nam)).failed is True:
        return False

    return True


def deploy():
    """Deploys the web static content to the web servers"""

    file = do_pack()
    if file is None:
        return False

    return do_deploy(file)
