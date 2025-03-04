#!/usr/bin/env bash
#Bash script to setuup web servers for deployment

sudo apt-get -y update
sudo apt-get -y install nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "Hello World!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
    listen 80 default_server;
    listen [::]80 default_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
    	alias /data/web_static/current;
	index index.html index.htm;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}" > /etc/nginx/sites-available/default

service nginx restart

