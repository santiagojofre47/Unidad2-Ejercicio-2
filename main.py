from claseViajero import ViajeroFrecuente
from ManejadorViajero import ManejadorViajero
from claseMenu import Menu

def test():
    print('Abriendo test...')
    Viajero1 = ViajeroFrecuente(1,'44127975','Santiago','Jofre',1000)
    Viajero2 = ViajeroFrecuente(2,'11122233','Juan','Castilo',2000)
    print(' === ANTES DE ACUMULAR ===')
    print(Viajero1.cantidadTotalMillas())
    print(' === DESPUES DE ACUMULAR ===')
    Viajero1.AcumularMillas(1000)
    print(Viajero1.cantidadTotalMillas())
    print(Viajero2)
    Viajero2.CanjearMillas(3000)#caso incorrecto
    print('Cerrando test...\n\n')

if __name__ == '__main__':
    test()
    lista = ManejadorViajero()
    menu = Menu()
    lista.crearInstancias()
    print(lista)
    numero_viajero = int(input('Ingrese un numero de viajero: '))
    viajero = lista.buscarViajero(numero_viajero)
    if type(viajero) == ViajeroFrecuente:
        menu.showMenu(viajero)
    else:
        print('ERROR: Viajero no encontrado!')
    


    