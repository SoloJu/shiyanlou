#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

CODE = 'utf-8'
HOST = ''
PORT = 21556
SIZE = 5
BUFSIZE = 1024
get_host = socket.gethostname()
ADDR = (get_host, PORT)

s_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_socket.bind(ADDR)
s_socket.listen(SIZE)
while True:
    print('Server started, listening client connection...')
    conn, addr = s_socket.accept()
    print('The connection address: ', addr)
    while True:
        try:
            data = conn.recv(BUFSIZE)
        except Exception:
            print('Broken client ', addr)
            break
        print('Client content: ', data.decode(CODE))
        if not data:
            break
        msg = time.strftime('%Y-%m-%d %X')
        msg1 = '[%s]:%s' % (msg, data.decode(CODE))
        conn.send(msg1.encode(CODE))
    conn.close()
s_socket.close()
