#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

CODE = 'utf-8'
HOST = '104.193.88.77'
PORT = 80
SIZE = 5
BUFSIZE = 1024
get_host = socket.gethostname()
ADDR = (HOST, PORT)

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c_socket.settimeout(3)
c_socket.connect(ADDR)
data = c_socket.recv(1024)
print(data)
