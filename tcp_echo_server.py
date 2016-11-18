#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('0.0.0.0', 2222))
sock.listen(1)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    if data == 'close':
        break
    conn.send(data)

conn.close()
