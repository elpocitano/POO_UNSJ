class Email:
    listamail= []

    __idCuenta: ' '
    __dominio: ' '
    __tipoDominio: ''
    __contrasenia: ' '

    def __init__(self,idCuenta="alumnopoo",dominio="gmail", tipoDominio="com", contrasenia="contreseña"):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasenia = contrasenia
        print("Estoy en el init")
        Email.listamail.append(self)

    def retornaEmail(self):
        return f"{self.__idCuenta}@{self.__dominio}.{self.__tipoDominio}"

    def crearCuenta(self, direccion):
        print("estoy enel crear cuenta")
        usuario=direccion.split("@")
        self.__idCuenta=usuario[0]
        self.__dominio=usuario[1].split(".")[0]
        self.__tipoDominio=usuario[1].split(".")[1]
        self.__contrasenia=input("Ingrese su contraseña para crear: ")


    def getDominio(self):
        return self.__dominio
        
    def cambiarContrasenia(self):
        print(" CAMBIO DE CONTRASEÑA ")
        contrasenia_actual = input("Ingrese la contraseña actual: ")
        if contrasenia_actual == self.__contrasenia:
            nueva_contrasenia = input("Ingrese la nueva contraseña: ")
            self.__contrasenia = nueva_contrasenia
            print("La contraseña ha sido cambiada exitosamente.")
        else:
            print("La contraseña ingresada es incorrecta.")
    
    @classmethod
    def instanciarcsv:
    with open(direcciones.csv, 'r') as f:
        reader=csv.reader(f)
        mail_list = list(reader)
        
        for mail in mail_list:
            if((mail[0]!= None) and (mail[1]!= None) and (mail[2]!= None) and (mail[3]!= None)):
               Email(
                __idCuenta= mail[0]
                __dominio=mail[1]
                __tipoDominio=mail[2]
                __contrasenia=mail[3]
               )
            else: print("Error, email inválido.")
    