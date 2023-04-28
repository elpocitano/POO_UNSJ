# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 01
Luna Juan Marcelo
DNI 24234578
@author: elpocitano@gmail.com
"""
import csv
from viajero_frecuente import ViajeroFrecuente


if __name__ == '__main__':

    """
Implemente un programa que:
    01- Leer de un archivo separado por comas los datos para crear instancias de la clase 
    ViajeroFrecuente, y almacenarlos en una lista.
"""
lista_viajeros = []
try:
    with open("lista_viajeros.csv") as archivo:
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            viajero = ViajeroFrecuente(int(fila[0]), int(fila[1]), str(fila[2]), str(fila[3]), int(fila[4]))
#            print(viajero.get_viajero())
            lista_viajeros.append(viajero)
except FileNotFoundError:
    print("El archivo lista.csv no se encontró")

for viajero in lista_viajeros:
    print(viajero.get_viajero())


"""
2- El usuario ingresa por teclado un número de viajero frecuente, el sistema presente un menú con:
    a- Consultar Cantidad de Millas.
    b- Acumular Millas.
    c- Canjear Millas.
"""
numero_viajero = int(input("Ingrese numero de viajero, 0 para salir: \n"))
while numero_viajero != 0:
    viajero_existe = False
    for viajero in lista_viajeros:
        if viajero.get_num_viajero() == numero_viajero:
            viajero_existe = True
            consulta = input(""" Ingrese la opción:
                            a- Consultar Cantidad de Millas.
                            b- Acumular Millas.
                            c- Canjear Millas. \n""").lower()
            if consulta == "a":
                print(viajero.get_millas_acumuladas())
            elif consulta == "b":
                millas_acumular = int(input("Ingrese la cantidad de millas a acumular: \n"))
                viajero.acumular_millas(millas_acumular)
            elif consulta == "c":
                millas_canje = int(input("Ingrese la cantidad de millas a canjear: \n"))
                viajero.canjear_millas(millas_canje)
            else:
                # Eligio una opción diferente a, b, 10c.
                print("La opción ingresada es invalida.\n")
    if not viajero_existe:
        # No encontró el número de viajeros.
        print("Viajero no encontrado.\n")
    # Actualizamos el valor de la condición del while (si no, bucle infinito)
    numero_viajero = int(input("Ingrese numero de viajero, 0 para salir:\n"))

print("No desea seguir buscando viajeros. Se vemos!!!\n")


"""
3- Represente el almacenamiento en memoria para la lista cargada con 4 viajeros.
"""
"""

4- Realice el Diagrama de Secuencia que corresponde a cada una de las siguientes funcionalidades:
4.1- El usuario elige la opción Acumular Millas, el sistema solicita el número de viajero frecuente 
y la cantidad de millas, el sistema busca el viajero, si lo encuentra acumula las millas ingresadas, 
e informa el nuevo total de millas acumulada; si el sistema no encuentra el viajero frecuente, informa 
al usuario de tal situación.

4.2- El usuario elige la opción Canjear Millas, el sistema solicita el número de viajero frecuente y 
la cantidad de millas a canjear, el usuario ingresa número de viajero frecuente y cantidad de millas 
a canjear, el sistema busca el viajero frecuente, si lo encuentra, verifica que la cantidad de millas 
acumuladas alcancen  para el canje, si no alcanzan informa la situación al usuario, si alcanzan hace 
el canje e informa al usuario que pudo realizar el canje y muestra la nueva cantidad de millas acumuladas; 
si el viajero frecuente no existe, el sistema informa al usuario de tal situación.
"""
