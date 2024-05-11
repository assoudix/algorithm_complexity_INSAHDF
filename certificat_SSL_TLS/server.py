#!/usr/bin/python3

import socket
import ssl
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('172.18.40.225', 9999))
server_socket.listen(5)
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile='cert.pem', keyfile='key.pem')
while True:
    client_socket, client_address = server_socket.accept()
    secure_socket = context.wrap_socket(client_socket, server_side=True)
    try:
        data = secure_socket.recv(1024)
        secure_socket.sendall(data)
    except Exception as e:
        print(f"Erreur de communication: {e}")
    finally:
        secure_socket.close()
        server_socket.close()