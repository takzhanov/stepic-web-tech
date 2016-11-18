#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 2222))
sock.send(b'hello')
sock.recv(1024)
sock.send(b'close')
sock.close()
