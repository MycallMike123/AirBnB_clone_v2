#!/usr/bin/env python3

import os
from datetime import datetime
from fabric.api import *

def do_pack():
    local('sudo mkdir -p versions')

    time = datetime.now()
    time_string = time.strftime('%Y%m%d%H%M%S')
    
    local('tar -cvzf versions/web_static_{}.tgz web_static'.format(time_string))
    #local(f'tar -cvzf versions/web_static_{time_string}.tgz web_static')

    file_path = f"versions/web_static_{time_string}.tgz"
    file_size = os.path.getsize(file_path)
    print(f"web_static packed: {file_path} -> {file_size}Bytes")
