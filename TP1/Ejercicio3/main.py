""" Ejercicio 3 del TP 1 de IA 2 / Año 2022
- Cabrero García, Gabriel
- Mellimaci, Marcelo E
- Tous Maggini, Martín
OBTENCIÓN DE LA UBICACION OPTIMA PARA PICKING MEDIANTE ALGORITMO GENETICO:
Dada varias ordenes de pedidos, se empieza a probar distintas disposiciones para encontrar 
la ubicacion de cada objeto que tenga el menor costo 
"""
from genetico import *
from random import shuffle
import pdb
def main():
    """ Método main
    Punto de entrada donde se inicia el programa
    """
    print("\t Ejercicio 3 del TP 1 de IA 2 \n")
x= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
disposicion =  [shuffle(x),
                shuffle(x),
                shuffle(x),
                shuffle(x),
                shuffle(x),
                shuffle(x),
                shuffle(x),
                shuffle(x)]

orden =[[1,2,3,4,5,6,7,8,9,10],
        [1,2,3,4,5,6,13,14,15,16],
        [11,12,13,14,15,16,5,6,1,2,3],
        [4,5,6,7,8,9,10],
        [16,1,2,3,15,6,5,4],
        [1,3,4,7,5,3,7,8,9,10,12,15,16],
        [5,6,7,8,9,10,4],
        [5,6,7,8,9,10,2,11,13,14,15]]

genetico(disposicion,orden)