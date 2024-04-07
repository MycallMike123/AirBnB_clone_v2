#!/usr/bin/python3

"""Fabric script that generates a .tgz archive
from the contents of the web_static folder
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Creates a .tgz archive from the contents of the web_static folder"""

    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Format the date and time
    now = datetime.now()
    _archive_path = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Compress the of web_static folder into the archive
    res = local("tar -cvzf {} web_static".format(_archive_path))

    # Check if the archive has been correctly generated
    if res.failed:
        return None
    else:
        return _archive_path
