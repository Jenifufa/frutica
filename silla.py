class Silla:

    class Clase:
        EJECUTIVA = "Ejecutiva"
        ECONOMICA = "Economica"
    
    
    class Ubicacion:
        VENTANA = "Ventana"
        CENTRO = "Centro"
        PASILLO = "Pasillo"
    
    
    def __init__(self, pNumero, pClase, pUbicacion):
        self.__numero = pNumero
        self.__clase = pClase
        self.__ubicacion = pUbicacion
        self.__pasajero = None
    
    def asignarPasajero(self, pPasajero):
        self.__pasajero = pPasajero
    
    def desasignarSilla(self):
        self.__pasajero = None
    
    def sillaAsignada(self):
        return self.__pasajero is not None
    
    def darNumero(self):
        return self.__numero
    
    def darClase(self):
        return self.__clase
    
    def darUbicacion(self):
        return self.__ubicacion
    
    def darPasajero(self):
        return self.__pasajero