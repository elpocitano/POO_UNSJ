# -*- coding: utf-8 -*-
"""
POO 2023 - Unidad 02 Ejercicio 01
Luna Juan Marcelo
DNI 24234578

@author: elpocitano@gmail.com
"""
import csv
from ClaseEmail import Email

if __name__ == '__main__':

    print("01- Ingresar el nombre de una persona y su dirección de e-mail (instancia de la clase Email)")
    email1 = Email()
    nombre = input("Ingrese su nombre: ")
    direccion = input("Ingrese su dirección de correo electrónico: ")
    email1.crear_cuenta(direccion)

    print("Luego imprima el siguiente mensaje:")
    print("Estimado <nombre> te enviaremos tus mensajes a la dirección <dirección de correo>.")
    email1.saludo(nombre)

    print("02- Para la instancia creada en el ítem anterior, modificar la contraseña")
    pass_actual = input("Ingrese la contraseña actual (por defecto es contraseña: ")
    if email1.validar_contrasenia(pass_actual):
        pass_nueva = input("Ingrese la nueva contraseña: ")
        email1.cambiar_contrasenia(pass_actual, pass_nueva)
        print("Contraseña actualizada!!")
    else:
        print("La contraseña ingresada no coincide!!")

    print("03- Crear un objeto de clase Email, a partir de una dirección de correo")
    email2 = Email()
    email2.crear_cuenta("informatica.fcefn@gmail.com")
    email2.retorna_email()

    print("04- a) Leer de un archivo separado por comas 10 direcciones de email, crear las cuentas correspondientes,")
    print("solo para las direcciones válidas comprobadas con expresiones regulares, y guardarlas en una lista")

    lista_emails = []
    with open("lista.csv") as archivo:
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            email = Email()
            if email.validar_direccion(fila[0]):
                email.crear_cuenta(fila[0])
                lista_emails.append(email)
            else: 
                print("Sintaxis Email inválida: ", fila[0])

    n = 0
    for email in lista_emails:
        n += 1
        print("Cuenta valida numero: ", n)
        print(email.retorna_email())

    print("04- b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual al ingresado.")
    dominio = input("Ingrese un dominio a contabilizar: ")
    dominio_contador = 0
    for email in lista_emails:
        if email.get_dominio() == dominio:
            print("Email: ", email.retorna_email())
            dominio_contador += 1
    print(f"Se encontraron {dominio_contador} cuentas con el dominio {dominio}.")

    print("05 - Implementar una clase de pruebas, en este caso, pytestt.")
    pytestt
