from clase2 import ViajeroFrecuente



def BuscarViajero(lista, viajero):
    for i in range(len(lista)):
        if (lista[i].getnumviajero()==viajero):
            return

        else: print("NO SE ENCONTRO EL VIAJERO")



import csv
if __name__ == __main__:
    listaviajeros=[]
    archivo=open("viajeros.csv}")
    reader=csv.reader(archivo,delimiter=',')



num = int(input("Ingrese el numero de viajero frecuente"))
BuscarViajero(listaviajeros,num)


x=input("a Consultar millas, b ACumular millas, c Canjear")


if (x=='a'):
      BuscarViajero(listaviajeros,num)
  elif(x=='b'):




