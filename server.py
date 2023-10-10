#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname()
port = 4444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept

    print("connection from " % str(address))

    message = 'hello thank you for connecting to the server' + "\r\n"

    clientsocket.close()
