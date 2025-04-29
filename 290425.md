__author__ = "Jenifer Daniela Urbano Córdoba"
__license__= "GPL"
__version__ = "1.0.0"
__email__ = "jenfier.urbano@campusucc.edu.co"

import random


class Curso:
    
    TOTAL_EST = 12

    def __init__(self,):
        self.__notas = []
    # Calcular la mayor nota del curso:
    def calcularMayorNota(self):
        mayorNota = 0.0
        for nota in self.__notas:
            if nota > mayorNota:
                mayorNota = nota
        return mayorNota


    # Aumentar el 5% todas las notas del curso, sin que ninguna de ellas sobrepase el valor 5,0:
    def HacerCurva(self):
        for i in range (len (self.TOTAL_EST)):
            nuevaNota = self.__notas[i] * 1.05
            if nuevaNota > 5.0:
                nuevaNota = 5.0
            self.__notas[i] = nuevaNota
            return self.__notas[i]
