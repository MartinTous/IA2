from random import random

class individuo():
    def __init__(self,list,ordenes):
        # individuo
        self.disposicion = list
        # Fitness del individuo
        self.fitness = self.setfitness(ordenes)
    def setfitness(self,ordenes):
        #calculo el fitness con recocido simulado
        fitness = 0
        for i in range (len(ordenes)):
            nf = recocido_simulado(self.disposicion,ordenes)
            fitness = fitness + nf
        return fitness
          


def genetico (disp,ordenes):
    poblacion = []
    for j in range(1000):
        for i in range(len(disp)):
            poblacion[i] = individuo(disp(i),ordenes)
        
        poblacion = seleccion(poblacion)
        poblacion = crossover(poblacion)
        poblacion = mutacion(poblacion)




    poblacion = seleccion(poblacion)
    pobok = []
    pobok = poblacion [1]

    print(pobok)








def seleccion(poblacion):
    sorted(poblacion, key=lambda poblacion: poblacion.fitness)
    for i in range(len(poblacion)/2):
        poblacion [i] = poblacion [i]
    return poblacion


def crossover(lista): 
  
    k = random.randint(0, len(lista[1]),2) 

    for i in range (len(lista)):
        for j in range(k,len(lista[i])): 
            lista[i][j], lista[i+1][j] = lista[i+1][j], lista[i][j]   
      
    return lista 

def mutacion (poblacion):
    for i in range(len(poblacion)):
        a = random.randint(0,len(poblacion[i])) 
        b = random.randint(0,len(poblacion[i]))
        c = random.randint(0,len(poblacion[i]))

        a1 = poblacion [i][a]
        a2 = poblacion [i][b]
        a3 = poblacion [i][c]

        poblacion [i][a] = a2
        poblacion [i][b] = a3
        poblacion [i][c] = a1
    
    return poblacion
