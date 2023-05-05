# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Integrador
Luna Juan Marcelo
DNI 24234578
Conjuntos
@author: elpocitano@gmail.com
"""


import numpy as np

class ManejadorAlumnos:
    def __init__(self):
        self.alumnos = []

    def buscar_alumno(self, dni):
    i = 0
    encontrado = None
    while i < len(self.alumnos) and not encontrado:
        if self.alumnos[i].dni == dni:
            encontrado = self.alumnos[i]
        else:
            i += 1
    return encontrado

    def agregar_alumno(self, alumno):
        self.alumnos.append(alumno)

    def cargar_datos(self, archivo):
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                campos = linea.strip().split(',')
                dni = int(campos[0])
                apellido = campos[1]
                nombre = campos[2]
                carrera = campos[3]
                anio = int(campos[4])
                alumno = Alumno(dni, apellido, nombre, carrera, anio)
                self.agregar_alumno(alumno)
