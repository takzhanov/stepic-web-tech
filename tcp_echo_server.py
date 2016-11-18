#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 2222))
sock.listen(10)

goNext = True
while goNext:
    conn, addr = sock.accept()
    print('connected:', addr)
    while True:
        data = conn.recv(1024)
        print(data)
        if not data:
            print('None', addr)
            break
        if data == b'close':
            goNext = False
            print('close', addr)
            break
        conn.send(data)
        # break # для прохода мультпиоточного. обманка
    conn.close()
