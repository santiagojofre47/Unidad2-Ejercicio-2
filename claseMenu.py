from claseViajero import ViajeroFrecuente

class Menu:
    __op =  None
    def __init__(self, opcion = None):
        self.__op = opcion
    

    def showMenu(self,viajero):
        cerrar = False
        while cerrar == False:
            print('\n\n\t\tMenu de opciones:\n')
            print('a- Consultar Cantidad de Millas\n')
            print('b- Acumular Millas.\n')
            print('c- Canjear Millas.\n')
            print('d- salir\n')
            self.__op = input('Seleccione una opcion: ')

            if self.__op == 'a' and type(viajero) == ViajeroFrecuente:
                print('Cantidad de millas: {}'.format(viajero.cantidadTotalMillas()))              
            elif self.__op == 'b' and type(viajero) == ViajeroFrecuente:
                millas = int(input('Ingrese la cantidad de millas a acumular: '))
                viajero.AcumularMillas(millas)
                print('Cantidad de millas acumuladas: {}'.format(viajero.cantidadTotalMillas()))
            elif self.__op == 'c' and type(viajero) == ViajeroFrecuente:
                millas = int(input('Ingrese la cantidad de millas a canjear: '))
                viajero.CanjearMillas(millas)
                print('cantidad de millas actual: {}' .format(viajero.cantidadTotalMillas()))
            elif self.__op == 'd':
                print('Cerrando menu...')
                cerrar = True
            else:
                print('ERROR: Opcion ingresada invalida!')    
                input('Presione ENTER para continuar...')   