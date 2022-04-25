from random import random

class individuo():
    def __init__(self,list):
        # individuo
        self.disposicion = list
        # Fitness del individuo
        self.fitness = self.setfitness()
    def setfitness():
        #calculo el fitness con recocido simulado
        pass   


def genetico (disp):
    poblacion = []
    for i in range(len(disp)):
        poblacion[i] = individuo(disp(i))
        

    for j in range(1000):
        poblacion = seleccion(poblacion)
        
        for i in range(len(poblacion)):
            a = random(0,len()) 
            b = random(0,len())
            c = random(0,len())

            a1 = poblacion [i][a]
            a2 = poblacion [i][b]
            a3 = poblacion [i][c]

            poblacion [i][a] = a2
            poblacion [i][b] = a3
            poblacion [i][c] = a1

            poblacion [i + len(poblacion)][a] = a3
            poblacion [i + len(poblacion) + 1][b] = a1
            poblacion [i + len(poblacion) + 2][c] = a2


    poblacion = seleccion(poblacion)
    pobok = []
    pobok = poblacion [1]

    print(pobok)

def seleccion(poblacion):
    sorted(poblacion, key=lambda x: x.fitness)
    for i in range(len(poblacion)/2):
        poblacion [i] = poblacion [i]
    return poblacion