#!/usr/bin/env python3

# password-generator.py

import string
import random
import argparse

def generate_password(numbers, symbols, length):
    # Define the characters to be used in the password
    characters = string.ascii_letters
    if numbers:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(numbers, symbols, length, count=5):
    passwords = []
    for _ in range(count):
        password = generate_password(numbers, symbols, length)
        passwords.append(password)
    return passwords

if __name__ == '__main__':
    # Create the argument parser
    parser = argparse.ArgumentParser(description='Generate passwords')
    parser.add_argument('-n', '--numbers', action='store_true', help='Include numbers')
    parser.add_argument('-s', '--symbols', action='store_true', help='Include symbols')
    parser.add_argument('-l', '--length', type=int, default=8, help='Length of password')
    parser.add_argument('-c', '--count', type=int, default=5, help='Number of passwords to generate')

    # Parse the command-line arguments
    args = parser.parse_args()

    # Generate the passwords
    passwords = generate_passwords(args.numbers, args.symbols, args.length, args.count)

    # Print the passwords
    for password in passwords:
        print(password)
