# Задачи и практикум по курсу [Web-технологии](https://stepik.org/s/n1ByvdqO)

Remote server via terminal. User box

    git clone https://github.com/takzhanov/stepic-web-tech.git /home/box/web \
        && cd web
    . ./prep-env.sh #change manually
    . ./init.sh

    # change settings.py Debug=False, ALLOWED_HOSTS=['*']
    curl http://localhost/hello?sd=ds
    curl http://localhost/question/324

Список задач:

* [Отдача статических файлов](https://stepik.org/s/x1y6kd4g)
    * поправить nginx.conf до 3f0035
* [TCP echo сервер](https://stepik.org/s/w1vQV0qj) 
    * python3 ./tcp_echo_server.py
