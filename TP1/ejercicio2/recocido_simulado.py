"""
Año 2022
- Cabrero García, Gabriel
- Mellimaci, Marcelo E
- Tous Maggini, Martín
"""

from random import sample, random
from math import e
from numpy import matrix
from a_estrella import a_estrella
from Aestrella import *

def almacen(matriz,dim):
    PF=0             #Pasillo filas
    PC=0             #Pasillos columnas
    estante=0
    for i in range(0,dim):
        matriz.append([0]*dim)

    for i in range(0,dim):
        for j in range(0,dim):
            if PF==0:
                matriz[i][j]=0
            elif PC==0:
                matriz[i][j]=0
            else:
                estante=estante+1
                matriz[i][j]=estante
            PC=PC+1
            if PC==3:
                PC=0
        PF=PF+1
        PC=0
        if PF==5:
            PF=0
    return matriz


#def buscar_ubicacion(plano, producto):
def ubicacion(matriz,pos):
    dim=len(matriz)
    #print(matrix(matriz))
    for i in range(0,dim):
        for j in range(0,dim):
            if matriz[i][j]==pos:
                #print(i,' ',j)
                pos=[i,j]
    return pos


def estado_vecino_aleatorio(estado_vecino):
    """ Función estado_vecino_aleatorio
    Crea un "estado vecino" de ordenamiento lista de productos intercambiando 
    aleatoriamente dos elementos de la lista
    Parametro de Entrada:
        lista_de_productos: lista de picking, con productos del almacen
    Parametro de Salida:
        estado_vecino: lista en que intercambio de lugar dos items aleatoriamente
    """
    # Creo una copia de la lista de productos que luego será el estado vecino
    #estado_vecino = lista_de_productos
    # Elijo aleatoriamente dos índices de la lista, e intercambio los elementos
    # para esos índices
    idx = range(len(estado_vecino))
    i1, i2 = sample(idx, 2)
    estado_vecino[i1], estado_vecino[i2] = estado_vecino[i2], estado_vecino[i1]
    return list(estado_vecino)


def distancia_recorrida(plano, lista_de_productos,dim):
    """ Función distancia_recorrida
    Calcula la distancia recorrida para un cierto orden de la lista de productos
    Es la función a minimizar. Dice que tan buena es una solución propuesta
    Parametros de Entrada:
        plano: Arreglo 2D con el mapa del almacen
        lista_de_productos: Lista de picking, con productos del almacen
    Parametro de Salida:
        distancia total recorrida para dicho ordenamiento de la lista de picking
    """
    posiciones = lista_de_productos[:]
    f_total = 0

    for i in range (len(posiciones) - 1):

        # Busco las coordenadas del elemento para poder buscarlo con A estrella
        indices_a = ubicacion(plano, posiciones[i])
        indices_b = ubicacion(plano, posiciones[i + 1])
       
        # Sumo de todos los desplazamientos de ir de cada posicion a la proximo
        f_total = f_total + len(Astar(plano, list(indices_a),list(indices_b )))
        plano=[]
        plano=almacen(plano,dim)
    return (f_total)


def recocido_simulado(To, alfa, Tf, plano, lista_de_productos,dim):
    """ Función recocido_simulado
    Determina un orden optimizado para la lista de picking a traves
    del algoritmo de Temple Simulado o Recocido Simulado
    Parametros de Entrada:
        To: Parametro Temperatura Inicial del algoritmo
        alfa: Factor que determina la velocidad de enfriamiento
        Tf: Parametro Temperatura Final, a la cual termina el bucle while
        plano: Arreglo 2D con el mapa del almacen
        lista_de_productos: Lista de picking, con productos del almacen
    Parametros de Salida:
        lista_de_productos: Lista ordenada para reducir la distancia recorrida
        dist_min: Distancia minimizada por la lista ordenada
    """
    plano=[]
    plano=almacen(plano,dim)
    e_actual = distancia_recorrida(plano, lista_de_productos,dim)

    # Temperatura inicial
    T = To
    while (T >= Tf):
        # La Temperatura va disminuyendo a medida que avanza el algoritmo
        T = alfa * T

        # Intercambio de lugar dos ítems diferentes de la lista
        estado_vecino = estado_vecino_aleatorio(lista_de_productos)

        plano=[]
        plano=almacen(plano,dim)
        e_estado_vecino = distancia_recorrida(plano, estado_vecino,dim)

                        
        # La variación de energía dE es la función objetivo a minimizar
        dE = e_estado_vecino - e_actual

        # Decrecimiento exponencial
        probabilidad = pow(e, -dE / T)

        # Los movimientos que minimizan la distancia recorrida se aceptan siempre
        # Si el nuevo estado candidato es peor, podría llegar a aceptarse con
        # probabilidad pow(e, -dE/T)
        if ((dE <= 0) or (probabilidad >= random())):
            e_actual=e_estado_vecino
            lista_de_productos=estado_vecino
            print(estado_vecino)
            print('Costo= ',e_estado_vecino)


    # El algoritmo devuelve la mejor solución que se haya podido explorar y la
    # distancia minimiaza correspondiente
    dist_min=e_actual
    return (lista_de_productos, dist_min)
    #[25, 33, 62, 27, 98, 66, 80, 95, 74, 29, 24, 63, 55, 70, 54, 22, 87, 47, 31, 72, 73, 65, 46, 58, 97]