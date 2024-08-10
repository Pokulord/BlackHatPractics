import socket 

# Хост, к которому будем подключаться

HOST = "www.google.com"
HOST_PORT = 80

# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((HOST, HOST_PORT))
# client.send(b"GET / HTTP/1.1\r\Host: google.com\r\n\r\n")

# response = client.recv(4096)
# print(response.decode())
# client.close()

# # Класс UDP-клиента
# class UDP_CLIENT:
#     def __init__(self) -> None:
#         pass

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
