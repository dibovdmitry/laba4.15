#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys

# Создание TCP/IP розетки.
rozetka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключение розетки к порту, который прослушивает сервер.
server_address = ('localhost', 8081)
print('Подключение к {} порт {}'.format(*server_address))
conn = rozetka.connect(server_address)


while True:
    command = input(">> ")
    print('Команда {!r}'.format(command))
    command_line = bytes(command, "utf-8")
    rozetka.sendall(command_line)
    data = rozetka.recv(512)
    if command == "exit":
        sys.exit()
    print("Received {!r}".format(data.decode("utf-8")))