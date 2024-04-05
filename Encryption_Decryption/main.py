#!/usr/bin/python3

'''added option to save the result into a file'''


from AES import *
from cesar import *
from vigenere import *
from RSA import *


def save_to_file(message):
    filename = input("Enter filename to save the result: ")
    with open(filename, "w") as file:
        file.write(message)
    print("Result saved to", filename)


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

    save_choice = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save_choice == "yes":
        save_to_file(encrypted)


if __name__ == "__main__":
    main()
