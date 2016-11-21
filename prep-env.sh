#!/usr/bin/env bash

sudo pip3 install django gunicorn
# поправить файлы gunicorn https://github.com/fedorch/stepic_web_project/blob/master/python3.md
sudo sed -i 's/bin\/python/bin\/python3/g' /usr/sbin/gunicorn*
sudo sed -i 's/bin\/python/bin\/python3/g' /usr/bin/gunicorn*
sudo sed -i 's/17.5/19.6/g' /usr/bin/gunicorn*
