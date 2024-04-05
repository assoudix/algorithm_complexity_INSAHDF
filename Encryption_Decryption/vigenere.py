#!/usr/bin/python3

"""simple vigenere cipher that calls back the cesar one, hence the import"""

from cesar import *

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