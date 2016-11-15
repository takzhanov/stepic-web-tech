#!/usr/bin/env bash
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo nginx -s reload
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
nohup gunicorn -b 0.0.0.0:8080 hello:app &
#sudo /etc/init.d/mysql start