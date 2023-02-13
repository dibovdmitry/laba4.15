#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
from time import perf_counter

# Создание TCP/IP розетки
rozetka = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Привязываем сокет к порту
server_address = ('localhost', 8081)
print('Старт сервера на {} порт {}'.format(*server_address))
rozetka.bind(server_address)

rozetka.listen(1)

while True:
    print('Ожидание соединения...')
    connection, client_address = rozetka.accept()
    start_time = 0
    try:
        print('Подключено к:', client_address)
        # Принимаем данные порциями и ретранслируем их
        while True:
            data = connection.recv(512)
            data_decode = data.decode("utf-8")
            print('Получено: {} '.format(data_decode))
            if data_decode == "on":
                msg = "Розетка в режиме='ON', напряжение='220V'".encode(encoding="utf-8")
                start_time = perf_counter()
                print('Отправление данных обратно клиенту.')
                connection.sendall(msg)
            elif data_decode == "off":
                mssg = f"Розетка в режиме='Off', время работы={perf_counter() - start_time:0.4f}"
                mssg_by = str(mssg).encode(encoding="utf-8")
                print('Отправление данных обратно клиенту.')
                connection.sendall(mssg_by)
            elif data_decode == "exit":
                print("Завершение работы сервера")
                connection.close()
                sys.exit()

            else:
                print('Нет данных от:', client_address)
                break

    finally:
        # Очищаем соединение
        connection.close()