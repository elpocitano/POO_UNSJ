# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 01
Luna Juan Marcelo
DNI 24234578

@author: elpocitano@gmail.com
"""
import re
class Email:
    __id_cuenta = str
    __dominio = str
    __tipo_dominio = str
    __contrasenia = str
    __nombre = str

    def __init__(self, id_cuenta='alumno', dominio='gmail', tipo_dominio='.com', contrasenia='contraseña'):
        self.__id_cuenta = id_cuenta
        self.__dominio = dominio
        self.__tipo_dominio = tipo_dominio
        self.__contrasenia = contrasenia

    def retorna_email(self):
        return f"Email: {self.__id_cuenta}@{self.__dominio}.{self.__tipo_dominio}"

    def crear_cuenta(self, direccion):
        usuario = direccion.split("@")
        self.__id_cuenta = usuario[0]
        self.__dominio = usuario[1].split(".")[0]
        self.__tipo_dominio = usuario[1].split(".")[1]

    def get_dominio(self):
        return self.__dominio

    def cambiar_contrasenia(self):
        pass_actual = input(
            "Ingrese la contraseña actual (por defecto es contraseña: ")
        if self.__contrasenia == pass_actual:
            pass_nueva = input("Ingrese la nueva contraseña: ")
            self.__contrasenia = pass_nueva
            print("Contraseña actualizada!!")
        else:
            print("La contraseña ingresada no coincide!!")

    def saludo(self, nombre):
        print(
            f"{nombre}, enviaremos tus mensajes a la dirección {self.retorna_email()}.")

    def validar_direccion(self, direccion):
        # Comprobar si la dirección de correo electrónico cumple con la estructura correcta
        # y contiene solo caracteres válidos
        validacion: bool = True
        expresion_regular = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        caracteres_validos = set(
            'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789._%+-@')
        if (not re.match(expresion_regular, direccion)) or (not (set(direccion) <= caracteres_validos)):
            validacion = False
        return validacion
