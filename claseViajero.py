class ViajeroFrecuente:
    __num_viajero = None
    __dni = None
    __nombre = None
    __apellido = None
    __millas_acum = None

    def __init__(self, numViajero = None, dni = None, nombre = None, apellido = None, millas = None):
        self.__num_viajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas

    def __str__(self):
        s = 'Numero Viajero: {}\nDNI: {}\nNombre: {}\nApellido: {}\nMillas Acumuladas: {}' .format(self.__num_viajero,self.__dni,self.__nombre,self.__apellido,self.__millas_acum)
        return s    

    def obtenerNumeroViajero(self):
        return self.__num_viajero    

    def cantidadTotalMillas(self):
        return self.__millas_acum

    def AcumularMillas(self,cantidadMillas):
        if type(cantidadMillas) == int:
            self.__millas_acum += cantidadMillas

    def CanjearMillas(self,cantidadMillas):
        if type(cantidadMillas) == int:
            if self.__millas_acum >= cantidadMillas:
                self.__millas_acum -= cantidadMillas
            else:
                print('ERROR: La cantidad de millas a canjear supera  la cantidad de millas acumuladas')                 