import random
from recocido_simulado import recocido_simulado
import pdb
from numpy import full

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
        """       print('\n')
        for i in range(0,16):                                                                 #_Graficar el almacén y el recorrido
            for j in range(0,16):
                print(plano[i][j],end=' ')
            print('\n') """
        for i in range (len(ordenes)):
            nf = recocido_simulado(plano,ordenes[i])[1]
            fitness = fitness + nf                                  #Acumulo todos los costos y ese es el fitness del individuo
        return fitness
          


def genetico (disp,ordenes):
    it = 0
    ft = full((10*len(disp),1),None) 
    arreglo = disp
    poblacion=[0,0,0,0]
    for j in range(4):                                           #Criterio de parada, cantidad de iteraciones
        for i in range(len(disp)):
            print(i)
            ind = individuo(arreglo[i],ordenes)               #Creo un objeto de cada individuo con su fitness asociado
            poblacion[i]= ind
            ft [it] = ind.fitness                          #Guardo los fitness en una lista para graficar al final
            it += 1
        poblacion = seleccion(poblacion) 
        print(poblacion)     
        nuevapoblacion = crossover(poblacion)
        print(nuevapoblacion)
        nuevapoblacion = mutacion(nuevapoblacion)
        print(nuevapoblacion)
        nuevapoblacion = poblacion + nuevapoblacion

        arreglo = nuevapoblacion


    for i in range(len(disp)):
        print(i)
        ind = individuo(disp[i],ordenes)
        poblacion[i]= ind 

    poblacion = seleccion(poblacion)                                #Hago una ultima seleccion para elegir al mejor de la ultima poblacion

    pobok = full((120,1),None)
    pobok = poblacion [1].disposicion


    print(pobok)




def seleccion(poblacion):
    poblacion.sort(key=lambda x: x.fitness)                          #Ordeno a la poblacion de forma ascendente segun su fitness
    seleccion=[0,0]
    for i in range(0,int(len(poblacion)/2)):                                #Seleciono la mitad con mejor fitness
        seleccion [i] = poblacion [i].disposicion
    return seleccion


def crossover(lista): 
    nuevalista=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    listadoble=[]
    k1 = random.randint(0, 120)                           #Punto random para entrecruzar
    k2 = random.randint(0, 120)
    while(k1==k2):
        k1 = random.randint(0, 120)                           #Punto random para entrecruzar
        k2 = random.randint(0, 120)
    if k1>k2: 
        k1,k2 = k2,k1   
    for i in range (0,len(lista),2):
        print()
        for j in range(k1,k2+1): 
            nuevalista[i][j], nuevalista[i+1][j] = lista[i+1][j], lista[i][j] 
        listadoble= lista[i]+lista[i+1]
        for h in range(k2+1,len(nuevalista)):
            pp=0
            for l in range(len(listadoble)):
                for j in range(len(nuevalista[i])):
                    if listadoble[l]!=nuevalista[i][j]:
                        nuevalista[i][h]=listadoble[l]
                        pp=1
                        break
                if pp==1:
                    break

        for h in range(k1-1):
            pp=0
            for l in range(len(listadoble)):
                for j in range(len(nuevalista[i])):
                    if listadoble[l]!=nuevalista[i][j]:
                        nuevalista[i][h]=listadoble[l]
                        pp=1
                        break
                if pp==1:
                    break
        for h in range(k2+1,len(nuevalista)):
            pp=0
            for l in range(len(listadoble)):
                for j in range(len(nuevalista[i+1])):
                    if listadoble[l]!=nuevalista[i+1][j]:
                        nuevalista[i+1][h]=listadoble[l]
                        pp=1
                        break
                if pp==1:
                    break

        for h in range(k1-1):
            pp=0
            for l in range(len(listadoble)):
                for j in range(len(nuevalista[i+1])):
                    if listadoble[l]!=nuevalista[i+1][j]:
                        nuevalista[i+1][h]=listadoble[l]
                        pp=1
                        break
                if pp==1:
                    break
      
    return nuevalista 

def mutacion (poblacion):               
    for i in range(len(poblacion)):
        a = random.randint(0,len(poblacion[i]))                     #elijo 3 puntos y realizo permutacion
        b = random.randint(0,len(poblacion[i]))
        c = random.randint(0,len(poblacion[i]))

        poblacion[i][a],poblacion [i][b], poblacion [i][c] = poblacion [i][b], poblacion [i][c],poblacion [i][a]
    return poblacion
