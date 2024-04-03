#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os

from base64 import b64encode, b64decode


def caesar_encrypt(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                shifted = ((shifted - ord('a')) % 26) + ord('a')
            elif char.isupper():
                shifted = ((shifted - ord('A')) % 26) + ord('A')
            encrypted_message += chr(shifted)
        else:
            encrypted_message += char
    return encrypted_message


def caesar_decrypt(encrypted_message, shift):
    return caesar_encrypt(encrypted_message, -shift)


def vigenere_encrypt(message, key):
    encrypted_message = ''
    key_length = len(key)
    for i, char in enumerate(message):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            encrypted_message += caesar_encrypt(char, shift)
        else:
            encrypted_message += char
    return encrypted_message

def vigenere_decrypt(encrypted_message, key):
    decrypted_message = ''
    key_length = len(key)
    for i, char in enumerate(encrypted_message):
        if char.isalpha():
            shift = ord(key[i % key_length].lower()) - ord('a')
            decrypted_message += caesar_decrypt(char, shift)
        else:
            decrypted_message += char
    return decrypted_message

def generate_aes_key(key_length=16):
    # Generate random bytes
    key_bytes = os.urandom(key_length)
    # Encode bytes as a string for convenience
    aes_key = key_bytes.hex()
    return aes_key

def aes_encrypt(message):
    # Generate a random AES key
    aes_key = generate_aes_key()
    cipher = AES.new(aes_key.encode(), AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(message.encode(), AES.block_size))
    iv = b64encode(cipher.iv).decode('utf-8')
    ct = b64encode(ct_bytes).decode('utf-8')
    return aes_key, iv, ct

def aes_decrypt(iv, ct, key):
    iv = b64decode(iv)
    ct = b64decode(ct)
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')

def generate_rsa_keys():
    key = RSA.generate(2048)
    public_key = key.publickey().export_key()
    private_key = key.export_key()
    return public_key, private_key

def rsa_encrypt(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def rsa_decrypt(encrypted_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()


def main():
    print("Choose encryption method:")
    print("1. Caesar")
    print("2. Vigenere")
    print("3. AES")
    print("4. RSA")
    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted = caesar_encrypt(message, shift)
        print("Encrypted:", encrypted)
        decrypted = caesar_decrypt(encrypted, shift)
        print("Decrypted:", decrypted)

    elif choice == 2:
        message = input("Enter the message to encrypt: ")
        key = input("Enter the key: ")
        encrypted = vigenere_encrypt(message, key)
        print("Encrypted:", encrypted)
        decrypted = vigenere_decrypt(encrypted, key)
        print("Decrypted:", decrypted)

    elif choice == 3:
        message = input("Enter the message to encrypt: ")
        aes_key, iv, ct = aes_encrypt(message)
        print("AES Key:", aes_key)
        print("Encrypted:", ct)
        decrypted = aes_decrypt(iv, ct, aes_key)
        print("Decrypted:", decrypted)

    elif choice == 4:
        message = input("Enter the message to encrypt: ")
        public_key, private_key = generate_rsa_keys()
        print("Public Key:")
        print(public_key.decode())
        print("\nPrivate Key:")
        print(private_key.decode())
        encrypted = rsa_encrypt(message, public_key)
        print("Encrypted:", encrypted)
        decrypted = rsa_decrypt(encrypted, private_key)
        print("Decrypted:", decrypted)

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()