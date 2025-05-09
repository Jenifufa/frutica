from silla import Silla
from pasajero import Pasajero

class Avion:

    # Atributos

    def __init__(self):  
        self.__sillas = []

        for i in range(1, 9):         #Sillas ejecutivas (1-8), dos filas con 4 sillas cada una (2 ventanas y 2 pasillos por fila)
            if i in [1, 4, 5, 8]:
                ubicacion = Silla.Ubicacion.VENTANA  # Ventana: sillas 1, 4, 5, 8
            else:
                ubicacion = Silla.Ubicacion.PASILLO  # Pasillo: sillas 2, 3, 6, 7
            
            # Silla ejecutiva
            self.__sillas.append(Silla(i, Silla.Clase.EJECUTIVA, ubicacion))
        
        for i in range(9, 51):        # Sillas económicas (9-50), 7 filas con 6 sillas cada una (2 ventanas, 2 centros, 2 pasillos por fila)

            posicion = (i - 9) % 6 + 1  # Calcular posición dentro de la fila (1-6)

            if posicion in [1, 6]:
                ubicacion = Silla.Ubicacion.VENTANA         # Ventana: posiciones 1 y 6
            elif posicion in [2, 5]:
                ubicacion = Silla.Ubicacion.CENTRO          # Centro: posiciones 2 y 5
            else: 
                ubicacion = Silla.Ubicacion.PASILLO         # Pasillo: posiciones 3 y 4
            
            # Silla económica
            self.__sillas.append(Silla(i, Silla.Clase.ECONOMICA, ubicacion))
    




    ####################################
    # Taller clase 2
    ####################################
    
    def contarSillasEjecutivasOcupadas(self):
        contador = 0
        for i in range(8):
            if self.__sillas[i].sillaAsignada():
                contador += 1
        return contador
    
    def buscarPasajeroEjecutivo(self, pCedula):
        for i in range(8):
            silla = self.__sillas[i]
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == pCedula:
                return silla
        return None
    
    def buscarSillaEconomicaLibre(self, pUbicacion):
        for i in range(8, len(self.__sillas)):
            silla = self.__sillas[i]
            if not silla.sillaAsignada() and silla.darUbicacion() == pUbicacion:
                return silla
        return None
    
    def asignarSillaEconomica(self, pUbicacion, pPasajero):
        silla = self.buscarSillaEconomicaLibre(pUbicacion)
        if silla is not None:
            silla.asignarPasajero(pPasajero)
            return True
        return False
    
    def anularReservaEjecutivo(self, pCedula):
        silla = self.buscarPasajeroEjecutivo(pCedula)
        if silla is not None:
            silla.desasignarSilla()
            return True
        return False
    
    def contarVentanasEconomica(self):
        contador = 0
        for i in range(8, len(self.__sillas)):
            silla = self.__sillas[i]
            if not silla.sillaAsignada() and silla.darUbicacion() == Silla.Ubicacion.VENTANA:
                contador += 1
        return contador
    
    def hayDosHomonimosEconomica(self):
        # Crear lista de nombres de pasajeros en clase económica
        nombres = []
        for i in range(8, len(self.__sillas)):
            silla = self.__sillas[i]
            if silla.sillaAsignada():
                nombre = silla.darPasajero().darNombre()
                # Si el nombre ya está en la lista, hay homónimos
                if nombre in nombres:
                    return True
                nombres.append(nombre)   # Agregar el nombre a la lista
        return False
    




    #-##################################
    # Tarea casa 3
    ####################################
    
    def contarSillasEconomicasLibres(self):
        contador = 0
        for i in range(8, len(self.__sillas)):
            if not self.__sillas[i].sillaAsignada():
                contador += 1
        return contador
    
    def contarPasilloEjecutivas(self):
        contador = 0
        for i in range(8):
            silla = self.__sillas[i]
            if not silla.sillaAsignada() and silla.darUbicacion() == Silla.Ubicacion.PASILLO:
                contador += 1
        return contador
    
    def desocuparAvion(self):
        for i in range(len(self.__sillas)):
            self.__sillas[i].desasignarSilla()
    






    #########################################################################
    # Métodos adicionales para poder hacer los ejemplos de la clase Pasajero
    #########################################################################
    
    #Para registrar un nuevo pasajero y asignarlo a una silla ejecutiva disponible
    def registrarPasajeroEjecutivo(self, pCedula, pNombre):
        nuevo_pasajero = Pasajero(pCedula, pNombre)    
        # Buscar una silla ejecutiva libre (cualquier ubicación)
        for i in range(8):
            silla = self.__sillas[i]
            if not silla.sillaAsignada():
                silla.asignarPasajero(nuevo_pasajero)
                return True
        
        return False  # Si no hay sillas ejecutivas disponibles
    
    # Método para buscar a un pasajero POR CEDULA en todo el avión
    def buscarPasajero(self, pCedula):
        for silla in self.__sillas:
            if silla.sillaAsignada() and silla.darPasajero().darCedula() == pCedula:
                return silla.darPasajero()
        return None
    
    # Ejemplo de método que utiliza la importación de Pasajero
    def crearListaPasajeros(self):
        lista_pasajeros = []
        
        for silla in self.__sillas:
            if silla.sillaAsignada():
                pasajero = silla.darPasajero()
                # diccionario para pasajero
                info = {
                    "cedula": pasajero.darCedula(),
                    "nombre": pasajero.darNombre(),
                    "clase": "Ejecutiva" if silla.darClase() == Silla.Clase.EJECUTIVA else "Económica",
                    "ubicacion": str(silla.darUbicacion()).split('.')[1],
                    "numero_silla": silla.darNumero()
                }
                lista_pasajeros.append(info)
        
        return lista_pasajeros

#######################################
# Ejemplo de uso de la clase Avion
#######################################

def main():
    # Crear el avión
    avion = Avion()
    
    # Registrar pasajeros
    avion.registrarPasajeroEjecutivo("123456", "Nicolas Maduro Moros")
    avion.registrarPasajeroEjecutivo("654321", "Miguel Polo Polo")
    
    # Crear un pasajero y asignarlo a silla económica
    pasajero = Pasajero("150508", "Wolfgang Amadeus Mozart")
    avion.asignarSillaEconomica(Silla.Ubicacion.VENTANA, pasajero)
    
    # Obtener lista de pasajeros
    lista = avion.crearListaPasajeros()
    print("Lista de pasajeros:")
    for p in lista:
        print(f"- {p['nombre']} (CC: {p['cedula']}), Clase: {p['clase']}, Silla: {p['numero_silla']}")
    
    # Probar métodos
    print(f"\nSillas económicas libres: {avion.contarSillasEconomicasLibres()}")
    print(f"Puestos disponibles en pasillos ejecutivos: {avion.contarPasilloEjecutivas()}")
    print(f"Sillas ejecutivas ocupadas: {avion.contarSillasEjecutivasOcupadas()}")

if __name__ == "__main__":
    main()