# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Integrador
Luna Juan Marcelo
DNI 24234578
Conjuntos
@author: elpocitano@gmail.com
"""


class ManejadorMaterias:
    def __init__(self):
        self.materias = []

    def agregar_materia(self, materia):
        self.materias.append(materia)

    def cargar_datos(self, archivo):
        with open(archivo, 'r') as f:
            lineas = f.readlines()
            for linea in lineas:
                campos = linea.strip().split(',')
                dni_alumno = int(campos[0])
                nombre = campos[1]
                fecha = campos[2]
                nota = float(campos[3])
                aprobacion = campos[4]
                materia = Materia(dni_alumno,
