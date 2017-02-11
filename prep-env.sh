#!/usr/bin/env bash

sudo pip3 install django gunicorn==17.5
# поправить файлы gunicorn https://github.com/fedorch/stepic_web_project/blob/master/python3.md
#sudo sed -i 's/bin\/python/bin\/python3/g' /usr/sbin/gunicorn*
#sudo sed -i 's/bin\/python/bin\/python3/g' /usr/bin/gunicorn*
#sudo sed -i 's/17.5/19.6/g' /usr/bin/gunicorn*

sudo chmod -R a+rw . #особенности проверяющей платформы, про доступ к базе видимо

sed -i 's/DEBUG = True/DEBUG = False/g' /home/box/web/ask/ask/settings.py
sed -i 's/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \['\''\*'\''\]/g' /home/box/web/ask/ask/settings.py