#!/usr/bin/python3

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