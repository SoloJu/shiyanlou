#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

CODE = 'utf-8'
HOST = ''
PORT = 21556
SIZE = 5
BUFSIZE = 1024
get_host = socket.gethostname()
ADDR = (get_host, PORT)

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.connect(ADDR)

while True:
    data = input('>>').strip()
    if not data:
        break
    c_socket.send(data.encode(CODE))
    data = c_socket.recv(BUFSIZE)
    if not data:
        break
    print(data.decode(CODE))
c_socket.close()
