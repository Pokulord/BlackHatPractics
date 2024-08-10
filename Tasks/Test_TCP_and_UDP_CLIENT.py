#! Задача 1, сделанная в рамках обучения BlackHat
# b перед строкой преобразует её в байтовый формат

import socket 

# Хост, к которому будем подключаться

HOST = "www.google.com"
HOST_PORT = 80

# Класс UDP-клиента
# UDP - протокол не поддерживает подключения
class UDP_CLIENT:
    def __init__(self) -> None:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.sendto(b"AAABBBCCC", ("127.0.0.1", 9997))
        # Принимаем данные 
        data, addr  = client.recvfrom(4096)

        print(data.decode())
        client.close()

# # Класс TCP-клиента
class TCP_CLIENT:
    def __init__(self) -> None:
        # Объект клиента
        # AF_INET - стандартное сетевое имя (адрес в формате IPv4)
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # Подключаем клиент
        client.connect((HOST, HOST_PORT))

        # Отправляем данные 
        client.send(b"GET / HTTP/1.1\r\Host: google.com\r\n\r\n")

        # Принимаем ответ
        response = client.recv(4096)

        print(response.decode())
        client.close()

if __name__ == "__main__":
    TCP_CLIENT()
    UDP_CLIENT()
