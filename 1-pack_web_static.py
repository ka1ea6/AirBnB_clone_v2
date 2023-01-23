#!/usr/bin/python3
'''Fabric script to generate a .tgz archive from
the contents of the web_static folder.'''


from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    '''Function to archive the web_static file'''
    dt = datetime.utcnow()

    file_name = f"versions/web_static\
    {dt.year}{dt.month}{dt.day}{dt.hour}{dt.minute}{dt.second}.tgz"

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local(f"tar -cfvz {file_name} web_static").failed is True:
        return None
    return file_name
