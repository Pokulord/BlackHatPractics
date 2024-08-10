# Многопоточный TCP-сервер

import socket 
import threading

# Параметры для подключения

IP = '0.0.0.0'
PORT = 9998

# class TCP_Sever:
#     def __init__(self) -> None:
#         server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         server.bind((IP, PORT))
#         # Не больше 5 активных соединений
#         server.listen(5)
#         print(f"LISTENING {IP}:{PORT}")
#         while True:
#             client, adress = server.accept()
#             print(f"[*] Accepted connection from : {adress[0]}: {adress[1]}")
#             # Создаём поток
#             client_handler = threading.Thread(target = handle_client,
#                                               args=(client,))
#             client_handler.start()
#     def handle_client(client_sock):
#         with client_sock as sock:
#             request = sock.recv(1024)
#             print(f"[*] Recieved : {request.decode('utf-8')}")
#             sock.send(b"ABC")
# if __name__ == "__main__":
#     TCP_Sever()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f"Listening {IP} : {PORT}")
    while True:
        client , adress = server.accept()
        print(f"Accepted connection from {adress[0]} : {adress[1]}")
        client_handler = threading.Thread(target = handle_client, args = (client, ))
        client_handler.start()

def handle_client(client_sock):
    with client_sock as sock:
        request = sock.recv(1024)
        print(f"[*] Recieved : {request.decode('utf-8')}")
        sock.send(b"ACK")

if __name__ == "__main__":
    main()