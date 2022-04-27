import csv
from claseViajero import ViajeroFrecuente

class ManejadorViajero:
    __lista = []

    def __init__(self):
        self.__lista = []

    def __str__(self):
        s = ''
        for viajero in self.__lista:
            s += str(viajero) + '\n\n'
        return s        

    def agregarViajero(self, unViajero):
        if type(unViajero) == ViajeroFrecuente:
            self.__lista.append(unViajero)

    def crearInstancias(self):
        archivo = open('ViajerosFrecuentes.csv')
        reader = csv.reader(archivo,delimiter=',')
        band = True
        for fila in reader:
            if band: 
                band = False
            else:
                numViajero = int(fila[0])
                millas = int(fila[4]) 
                unViajero = ViajeroFrecuente(numViajero,fila[1],fila[2],fila[3],millas)
                self.agregarViajero(unViajero)
        archivo.close()

    def buscarViajero(self, numero):#Metodo que busca en la lista de viajeros el objeto con el nummero de viajero dado, retorna el objeto de ese viajero
        encontro = False
        for i in range(len(self.__lista)):
            if numero == self.__lista[i].obtenerNumeroViajero():
                return self.__lista[i]
                break