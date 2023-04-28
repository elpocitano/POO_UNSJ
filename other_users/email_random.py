# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 01
Luna Juan Marcelo
DNI 24234578

@author: elpocitano@gmail.com
"""
import random
import string

valid_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "aol.com", "protonmail.net"]

def generate_random_username(length):
    """Generates a random username of the given length."""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_domain():
    """Generates a random domain from the list of valid domains."""
    return random.choice(valid_domains)

def generate_random_email():
    """Generates a random email address with a valid syntax."""
    username = generate_random_username(8)
    domain = generate_random_domain()
    return f"{username}@{domain}"

# Generate 10 random email addresses
for i in range(10):
    email = generate_random_email()
    print(email)

def generate_invalid_username(length):
    """Generates a random username with invalid characters."""
    letters = string.ascii_lowercase + ' !@#$%^&*()'
    return ''.join(random.choice(letters) for i in range(length))

def generate_invalid_domain():
    """Generates a random invalid domain."""
    letters = string.ascii_lowercase
    return f"{random.choice(letters)}{random.choice(letters)}{random.choice(letters)}"

# Generate one valid and one invalid email address
valid_email = generate_random_email()
invalid_email = f"{generate_invalid_username(10)}@{generate_invalid_domain()}"
print(valid_email)
print(invalid_email)