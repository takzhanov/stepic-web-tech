#!/usr/bin/env bash
#local
#ln -sf ~/dev/dev/stepic-web-tech /home/box/web
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
#sudo nginx -s reload
sudo mkdir -p /etc/gunicorn.d
sudo ln -sf /home/box/web/etc/hello-gunicorn.conf   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/echo-gunicorn.conf   /etc/gunicorn.d/echo.py
sudo /etc/init.d/gunicorn restart
#nohup gunicorn -b 0.0.0.0:8080 hello:app &
#sudo /etc/init.d/mysql start