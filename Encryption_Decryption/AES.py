#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
from base64 import b64encode, b64decode


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