from random import random
from recocido_simulado import recocido_simulado

class individuo():                                      
    def __init__(self,list,ordenes):
        # individuo
        self.disposicion = list
        # Fitness del individuo
        self.fitness = self.setfitness(ordenes)
    def setfitness(self,ordenes):
        #calculo el fitness con recocido simulado
        fitness = 0
        it=0
        plano =[[0,  0,  0, 0, 0, 0, 0, 0],
                [0,  1,  1, 0, 0, 1, 1, 0],
                [0,  1,  1, 0, 0, 1, 1, 0],
                [0,  1,  1, 0, 0, 1, 1, 0],
                [0,  1,  1, 0, 0, 1, 1, 0],
                [0,  0,  0, 0, 0, 0, 0, 0],]
        for i in range(len(plano)):
            for j in range(len(plano[i])):
                if plano[i][j]==1:
                    plano[i][j]== self.disposicion[it]
                    it += it
        for i in range (len(ordenes)):
            nf = recocido_simulado(plano,ordenes[i])[1]
            fitness = fitness + nf                                  #Acumulo todos los costos y ese es el fitness del individuo
        return fitness
          


def genetico (disp,ordenes):
    it = 0
    ft = []
    poblacion = []
    for j in range(1000):                                           #Criterio de parada, cantidad de iteraciones
        for i in range(len(disp)):
            poblacion[i] = individuo(disp(i),ordenes)               #Creo un objeto de cada individuo con su fitness asociado
            ft [it] = poblacion[i].fitness                          #Guardo los fitness en una lista para graficar al final
            it += it
        poblacion = seleccion(poblacion)                    
        poblacion = crossover(poblacion)
        poblacion = mutacion(poblacion)




    poblacion = seleccion(poblacion)                                #Hago una ultima seleccion para elegir al mejor de la ultima poblacion
    pobok = []
    pobok = poblacion [1]

    print(pobok)




def seleccion(poblacion):
    sorted(poblacion, key=lambda poblacion: poblacion.fitness)       # Ordeno a la poblacion de forma ascendente segun su fitness
    for i in range(len(poblacion)/2):                                #Seleciono la mitad con mejor fitness
        poblacion [i] = poblacion [i]
    return poblacion


def crossover(lista): 
    nuevalista=[0,0,0,0,0,0,0,0,0,0]
    listadoble=[]
    k1 = random.randint(0, len(lista[1]),2)                           #Punto random para entrecruzar
    k2 = random.randint(0, len(lista[1]),2)
    while(k1==k2):
        k1 = random.randint(0, len(lista[1]),2)                           #Punto random para entrecruzar
        k2 = random.randint(0, len(lista[1]),2)
    if k1>k2: 
        k1,k2 = k2,k1   
    for i in range (len(lista)):
        for j in range(k1,k2+1): 
            nuevalista[i][j], nuevalista[i+1][j] = lista[i+1][j], lista[i][j] 
        listadoble= lista[i]+lista[i+1]
        for l in range(len(listadoble)):
            for j in range(len(nuevalista)):
                if listadoble[l]!=nuevalista[j]:
                    nuevalista[j]==listadoble[l]
                    break
          
      
    return lista 

def mutacion (poblacion):               
    for i in range(len(poblacion)):
        a = random.randint(0,len(poblacion[i]))                     #elijo 3 puntos y realizo permutacion
        b = random.randint(0,len(poblacion[i]))
        c = random.randint(0,len(poblacion[i]))

        poblacion[i][a],poblacion [i][b], poblacion [i][c] = poblacion [i][b], poblacion [i][c],poblacion [i][a]
    return poblacion
