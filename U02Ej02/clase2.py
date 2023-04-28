class ViajeroFrecuente:
    __numviajero: int
    __dni: int
    __nombre: str
    __apellido: str
    __millas_acum: int

def __init__(self):
    __numviajero: None
    __dni: 0
    __nombre: None
    __apellido: None
    __millas_acum: -1

def getnumviajero(self):
    return self.__numviajero

def cantidadTotaldeMillas(self):
    return self.__millas_acum

def acumularMillas(self, suma):
    self.__millas_acum = self.__millas_acum+suma
    return cantidadTotaldeMillas()

def canjearMillas (self,cant):
    if(cantidadTotaldeMillas()<cant):
        self.__millas_acum=self.__millas_acum-cant
    else:
        print("No posee suficientes millas para realizar el canje.")

