#!/usr/bin/env bash
#script that sets up my web servers for deployment

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow "Nginx HTTP"

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/releases/test/index.html
echo "<html>
<head></head>
<body>hello there</body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo -ln -s /data/web_static/releases/test/ /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

sudo sed -i '/listen 80 default_sever/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart

