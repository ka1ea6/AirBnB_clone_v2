#!/usr/bin/python3
# Fabric script to distribute an archive to web servers

from fabric.api import put, env, run
import os.path

env.hosts = [""]


def do_deploy(archive_path):
    '''Deploys an archive to a web server'''

    if os.path.isfile(archive_path) is False:
        return False

    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, f"/tmp/{file}").failed is True:
        return False
    if run(f"rm -rf /data/web_static/releases/{name}/").failed is True:
        return False
    if run(f"mkdir -p /data/web_static/releases/{name}/").failed is True:
        return False
    if run(f"tar -xzf /tmp/{file} -C /data/web_static/releases/{name}").failed is True:
        return False
    if run(f"rm /tmp/{file}").failed is True:
        return False
    if run(f"mv /data/web_static/releases/{name}/web_static/* "
            f"/data/web_static/releases/{name}").failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(name)).failed is True:
        return False
    return True
