# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 01
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
from ClaseEmail import Email
import pytest

def test_crear_cuenta():
    email = Email()
    email.crear_cuenta('usuario@dominio.com')
    assert email.retorna_email() == "Email: usuario@dominio.com"

def test_retorna_email():
    email = Email('alumno', 'gmail', 'com', 'contraseña')
    assert email.retorna_email() == "Email: alumno@gmail.com"

def test_get_dominio():
    email = Email('alumno', 'gmail', 'com', 'contraseña')
    assert email.get_dominio() == "gmail"

def test_validar_contrasenia():
    email = Email('alumno', 'gmail', 'com', 'contraseña')
    assert email.validar_contrasenia('contraseña') == True
    assert email.validar_contrasenia('otra_contrasenia') == False

def test_cambiar_contrasenia():
    email = Email('alumno', 'gmail', 'com', 'contraseña')
    pass_actual = "contraseña"
    if email.validar_contrasenia(pass_actual):
        pass_nueva = "nueva_contraseña"
        email.cambiar_contrasenia(pass_nueva)
        assert email.validar_contrasenia(pass_nueva)
    else:
        assert False, "La contraseña ingresada no coincide"

def test_validar_direccion():
    email = Email()
    assert email.validar_direccion("user@example.com") == True
    assert email.validar_direccion("userexample.com") == False

def saludo(self, nombre):
    return f"{nombre}, enviaremos tus mensajes a la dirección {self.retorna_email()}."

