#!/usr/bin/python3

import ssl
import socket
context = ssl.create_default_context()
context.load_verify_locations('cert.pem')
with socket.create_connection(('172.18.47.225', 9999)) as sock:
    with context.wrap_socket(sock, server_hostname='OMAR') as secure_sock:
        secure_sock.sendall(b"Bonjour serveur!")
        data = secure_sock.recv(1024)
        print(f"Received: {data.decode()}")