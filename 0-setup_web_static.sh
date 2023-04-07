#!/usr/bin/env bash
# sets up a server for the deployment of a static page

# install nginx if it's not already installed
if [ ! -d /etc/nginx ]; then
    sudo apt-get update
    sudo apt-get install nginx -y
    sudo ufw allow "Nginx HTTP"
    sudo service nginx start
fi

# create the directories /data and /data/web_static if it doesn't exist
if [ ! -d /data/ ] || [ ! -d /data/web_static/ ]; then
    sudo mkdir -p /data/web_static/
fi

# create the directory /data/web_static/releases if it doesn't exist
if [ ! -d /data/web_static/releases ] || [ ! -d /data/web_static/releases/test/ ]; then
    sudo mkdir -p /data/web_static/releases/test/
fi

# create the directory /data/web_static/shared if it doesn't exist
if [ ! -d /data/web_static/shared ]; then
    sudo mkdir /data/web_static/shared/
fi

# create the file /data/web_static/releases/test/index.html if it doesn't exist
echo "<html>
     <head></head>
     <body>
	Holberton School
     </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# delete the directory /data/web_static/current if it exists
if [[ -L /data/web_static/current ]]; then
    sudo rm -rf /data/web_static/current
fi

# create a symbolic link /data/web_static/current to the /data/web_static/releases/test directory
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data directory and everything inside to the current user and group
sudo chown -R ubuntu:ubuntu /data/

# update nginx to serve the content of /data/web_static/current to hbnb_static

sudo sed -i "s/server_name _;/server_name _;\n\n\tlocation \/hbnb_static {\n\t\talias \/data\/web_static\/current\/;\n\t\ttry_files index.html 0-index.html =404;\n\t}/" /etc/nginx/sites-available/default

sudo service nginx restart
