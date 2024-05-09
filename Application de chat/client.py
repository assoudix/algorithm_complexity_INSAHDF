#!/usr/bin/python3

import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

# Client configuration
host = 'localhost'
port = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Receive the key and IV from the server
key_iv = client_socket.recv(32)  # 16 bytes for key, 16 bytes for IV
key = key_iv[:16]  # Extract the key
iv = key_iv[16:]  # Extract the IV

# Set up encryption and decryption
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
decryptor = cipher.decryptor()
pkcs7 = padding.PKCS7(128)  # AES block size is 128 bits

print("Connected to the server. Type 'exit' to quit.")

try:
    while True:
        # Get user input
        message = input("Enter a message: ")

        # Exit condition
        if message.lower() == 'exit':
            break  # Exit the loop and close the connection

        # Pad and encrypt the message
        padder = pkcs7.padder()
        padded_message = padder.update(message.encode('utf-8')) + padder.finalize()
        encrypted_message = encryptor.update(padded_message)

        # Send the encrypted message to the server
        client_socket.sendall(encrypted_message)

        # Receive encrypted response from the server
        encrypted_response = client_socket.recv(1024)
        if not encrypted_response:
            break  # Connection closed by the server

        # Decrypt and unpad the response
        decrypted_response = decryptor.update(encrypted_response)

        unpadder = pkcs7.unpadder()
        unpadded_response = unpadder.update(decrypted_response) + unpadder.finalize()

        print(f"Server says: {unpadded_response.decode('utf-8')}")

finally:
    client_socket.close()
    print("Client connection closed.")
