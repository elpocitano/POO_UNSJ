# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 03
Luna Juan Marcelo
DNI 24234578

@author: elpocitano@gmail.com
"""


class Registro:
    def __init__(self, temperatura, humedad, presion):
        self.__temperatura = temperatura
        self.__humedad = humedad
        self.__presion = presion

    def get_temperatura(self):
        return self.__temperatura

    def get_humedad(self):
        return self.__humedad

    def get_presion(self):
        return self.__presion
    
