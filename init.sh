#!/usr/bin/env bash

#for local
#ln -sf ~/dev/dev/stepic-web-tech /home/box/web

#nginx
sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

#gunicorn
sudo mkdir -p /etc/gunicorn.d
sudo ln -sf /home/box/web/etc/hello-gunicorn.conf   /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/etc/ask-gunicorn.conf   /etc/gunicorn.d/ask.py
sudo /etc/init.d/gunicorn restart

#db
#sudo /etc/init.d/mysql start
#mysql -u root -p < create-db
cd /home/box/web/ask
#sqlite3 ask.sqlite3
python3 manage.py migrate auth
python3 manage.py makemigrations
python3 manage.py migrate
cd -

#manual
#manage.py syncdb
