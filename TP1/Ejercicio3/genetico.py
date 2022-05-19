import random
import matplotlib.pyplot as plt
#import pdb
from numpy import full
from recocido_simulado import RecocidoSimulado

_recocido_simulado = RecocidoSimulado()

class individuo():
    def __init__(self,lista,ordenes):
        # individuo
        self.disposicion = lista
        # Fitness del individuo
        self.fitness = self.setfitness(ordenes)

    def setfitness(self,ordenes):
        #calculo el fitness con recocido simulado
        # pdb.set_trace()
        fitness = 0
        it=0
        plano =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
        for i in range(1, len(plano)-1):
            for j in range(1, len(plano[i])-1):
                if plano[i][j]==1:
                    plano[i][j] = self.disposicion[it]
                    it += 1
        
        #pdb.set_trace()

        for i in range (len(ordenes)):
            nf = _recocido_simulado.optimizar(plano,ordenes[i])[1]
            fitness = fitness + nf                                  #Acumulo todos los costos y ese es el fitness del individuo
        return fitness
          


def genetico (disp,ordenes):
    it = 0
    arreglo = disp
    ff = 1000
    promedio=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for j in range(30):                                       #Criterio de parada, cantidad de iteraciones
        print(j) 
        poblacion=[0,0,0,0,0,0,0,0,0,0,0,0]
        prom = 0                                
        for i in range(len(arreglo)):
            ind = individuo(arreglo[i],ordenes)               #Creo un objeto de cada individuo con su fitness asociado
            poblacion[i]= ind
            prom =  int(ind.fitness)
            if prom<ff:
                ff= prom
        promedio[j] = ff 
        poblacion = seleccion(poblacion)     
        nuevapoblacion = crossover(poblacion)
        #print(nuevapoblacion[0])
        #print(nuevapoblacion[1])
        nuevapoblacion = mutacion(nuevapoblacion)
        nuevapoblacion = poblacion + nuevapoblacion

        arreglo = nuevapoblacion

    poblacion=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(disp)):
        ind = individuo(arreglo[i],ordenes)
        poblacion[i]= ind 

    poblacion = seleccion(poblacion)                                #Hago una ultima seleccion para elegir al mejor de la ultima poblacion

    pobok = full((120,1),None)
    pobok = poblacion [1]
    print(pobok)
    x2=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    plt.plot(x2,promedio, "x")
    plt.show()


def seleccion(poblacion):
    poblacion.sort(key=lambda x: x.fitness)                          #Ordeno a la poblacion de forma ascendente segun su fitness
    seleccion=[0,0,0,0,0,0]
    for i in range(0,int(len(poblacion)/2)):                                #Seleciono la mitad con mejor fitness
        seleccion [i] = poblacion [i].disposicion
    return seleccion


def crossover(lista): 
    nuevalista=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    listadoble=[]
    k1 = random.randint(0, 119)                           #Punto random para entrecruzar
    k2 = random.randint(0, 119)
    while(k1==k2):
        k1 = random.randint(0, 119)                           #Punto random para entrecruzar
        k2 = random.randint(0, 119)
    if k1>k2: 
        k1,k2 = k2,k1   
    for i in range (0,len(lista),2):
        for j in range(k1,k2+1): 
            nuevalista[i][j], nuevalista[i+1][j] = lista[i+1][j], lista[i][j] 
        listadoble= lista[i]+lista[i+1]
                    

        for h in range(k1):
            for l in range(len(listadoble)):
                pp=0
                for j in range(len(nuevalista[i])):
                    if listadoble[l]==nuevalista[i][j]:
                        pp=1
                        break
                if pp!=1:
                    nuevalista[i][h]=listadoble[l]

        for h in range((k2+1),len(nuevalista[i])):
            for l in range(len(listadoble)):
                pp=0
                for j in range(len(nuevalista[i])):
                    if listadoble[l]==nuevalista[i][j]:
                        pp=1
                        break
                if pp!=1:
                    nuevalista[i][h]=listadoble[l]            



        for h in range(k1):
            for l in range(len(listadoble)):
                pp=0
                for j in range(len(nuevalista[i+1])):
                    if listadoble[l]==nuevalista[i+1][j]:
                        pp=1
                        break
                if pp!=1:
                    nuevalista[i+1][h]=listadoble[l]

        for h in range((k2+1),len(nuevalista[i+1])):
            for l in range(len(listadoble)):
                pp=0
                for j in range(len(nuevalista[i+1])):
                    if listadoble[l]==nuevalista[i+1][j]:
                        pp=1
                        break
                if pp!=1:
                    nuevalista[i+1][h]=listadoble[l] 


    return nuevalista 

def mutacion (poblacion):               
    for i in range(len(poblacion)):
        a = random.randint(0,len(poblacion[i])-1)                     #elijo 3 puntos y realizo permutacion
        b = random.randint(0,len(poblacion[i])-1)
        c = random.randint(0,len(poblacion[i])-1)

        poblacion[i][a],poblacion [i][b], poblacion [i][c] = poblacion [i][b], poblacion [i][c],poblacion [i][a]
    return poblacion
