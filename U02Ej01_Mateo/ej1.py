import Email from mail

if __name__ == '__main__':
    email1=Email()
    nombre=input("ingrese el nombre: ")
    direccion=input("ingrese direccion de correo: ")
    email1.crearCuenta(direccion)
    print (f"Estimado {nombre} te enviaremos tus mensajes a la direccion {direccion}")
    
    email1.cambiarContrasenia()

    email2=Email()
    direccion2=("informatica.fcefn@gmail.com")
    email2.crearCuenta(direccion2)
    print (email2.retornaEmail())
