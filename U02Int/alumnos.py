# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Integrador
Luna Juan Marcelo
DNI 24234578
Conjuntos
@author: elpocitano@gmail.com
"""


class Alumno:
    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.dni = dni
        self.apellido = apellido
        self.nombre = nombre
        self.carrera = carrera
        self.anio = anio
        self.materias_aprobadas = []

    def __lt__(self, otro):
        if self.anio != otro.anio:
            return self.anio < otro.anio
        else:
            return (self.apellido, self.nombre) < (otro.apellido, other.nombre)

    def agregar_materia_aprobada(self, materia):
        self.materias_aprobadas.append(materia)

    def calcular_promedio(self):
        notas = []
        for materia in self.materias_aprobadas:
            notas.append(materia.nota)
        promedio_con_aplazos = np.mean(notas)
        cant_aplazos = len([nota for nota in notas if nota < 4])
        promedio_sin_aplazos = np.mean([nota for nota in notas if nota >= 4])
        return (promedio_con_aplazos, promedio_sin_aplazos, cant_aplazos)