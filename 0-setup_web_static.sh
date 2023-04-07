#!/usr/bin/env bash
# sets up a server for the deployment of a static page

# install nginx if it's not already installed
if [ ! -d /etc/nginx ]; then
    sudo apt-get update
    sudo apt-get install nginx -y
    sudo ufw allow "Nginx HTTP"
    echo "server {
     listen 80 default_server;
     listen [::]:80 default_server;
     add_header X-Served-By $HOSTNAME;
     root /var/www/html;
     index index.html index.htm index.nginx-debian.html;
     server_name _;
     location /redirect_me {
     	      return 301 https://javascript.info;
	      }
     location / {
     	      try_files \$uri \$uri/ =404;
     }
     error_page 404 /error_page.html;
     location = /error_page.html {
     	      root /var/www/html;
	      internal;
      }
}" | sudo tee /etc/nginx/sites-available/default
    echo "Hello World!" | sudo tee /var/www/html/index.html
    echo "Ceci n'est pas une page" | sudo tee /var/www/html/error_page.html
    sudo service nginx start
fi

# create directories if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
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
