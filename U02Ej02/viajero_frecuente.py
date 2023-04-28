# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 01
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""


class ViajeroFrecuente:
    __num_viajero = int
    __dni = str
    __nombre = str
    __apellido = str
    __millas_acumuladas = int

    def __init__(self, num_viajero: int, dni: int, nombre: str, apellido: str, millas_acumuladas: int):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acumuladas = millas_acumuladas

    def get_viajero(self):
        return f"Viajero {self.get_num_viajero()} - DNI: {self.get_dni()} Nombre: {self.get_nombre()} {self.get_apellido()} - Millas acumuladas: {self.get_millas_acumuladas()}"

    def get_num_viajero(self):
        return self.__num_viajero

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_apellido(self):
        return self.__apellido

    def get_millas_acumuladas(self):
        return self.__millas_acumuladas

    def acumular_millas(self, millas):
        self.__millas_acumuladas += millas
        return self.get_millas_acumuladas()

    def canjear_millas(self, millas):
        if self.get_millas_acumuladas() < millas:
            self.__millas_acumuladas -= millas
        else:
            print("No posee suficientes millas para realizar el canje.")
        return self.get_millas_acumuladas()
