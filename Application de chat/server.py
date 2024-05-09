#!/usr/bin/python3

import socket
import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend


host = 'localhost'
port = 12345
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server_socket.bind((host, port))
server_socket.listen(1)  # Allow one connection in the queue

print("Server is listening.")

# Génération de la clé AES (random, 16 bits) et du vecteur d'initialisation
key = os.urandom(16)
iv = os.urandom(16)


client_socket, client_address = server_socket.accept()
print("Connected.")

# Envoi de la clé pour établir une connection sécurisée
client_socket.sendall(key + iv)

# Codage et Padding
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()
pkcs7 = padding.PKCS7(128)

#Boucle principale pour la communication

try:
    while True:

        encrypted_data = client_socket.recv(1024)
        if not encrypted_data:
            break


        decrypted_data = decryptor.update(encrypted_data)


        unpadder = pkcs7.unpadder()
        unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
        plaintext_message = unpadded_data.decode('utf-8')

        print(f"Client: {plaintext_message}")


        server_response = input("Your response: ")


        padder = pkcs7.padder()
        padded_response = padder.update(server_response.encode('utf-8')) + padder.finalize()
        encrypted_response = encryptor.update(padded_response)


        client_socket.sendall(encrypted_response)

finally:
    client_socket.close()
    server_socket.close()
    print("Server connection closed.")
