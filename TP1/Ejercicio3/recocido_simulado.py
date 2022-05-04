"""
Año 2022
- Cabrero García, Gabriel
- Mellimaci, Marcelo E
- Tous Maggini, Martín
"""

from random import random, choice
from math import e
from copy import deepcopy
import pandas as pd


def almacen(matriz, dim):
    # Pasillo filas
    PF = 0
    # Pasillos columnas
    PC = 0
    estante = 0
    for i in range(0, dim):
        matriz.append([0] * dim)

    for i in range(0, dim):
        for j in range(0, dim):
            if PF == 0:
                matriz[i][j] = 0
            elif PC == 0:
                matriz[i][j] = 0
            else:
                estante = estante + 1
                matriz[i][j] = estante
            PC = PC + 1
            if PC == 3:
                PC = 0
        PF = PF + 1
        PC = 0
        if PF == 5:
            PF = 0
    return matriz


def ubicacion(matriz, pos):
    dim = len(matriz)
    for i in range(0, dim):
        for j in range(0, dim):
            if matriz[i][j] == pos:
                pos = [i, j]
    return pos


def estado_vecino_aleatorio(lista_de_productos):
    """ Función estado_vecino_aleatorio
    Crea un "estado vecino" de ordenamiento lista de productos intercambiando 
    aleatoriamente dos elementos de la lista
    Parametro de Entrada:
        lista_de_productos: lista de picking, con productos del almacen
    Parametro de Salida:
        estado_vecino: lista en que intercambio de lugar dos items aleatoriamente
    """
    #estado_vecino = lista_de_productos
    # Elijo aleatoriamente dos índices de la lista, e intercambio los elementos
    # para esos índices
    # estado_vecino=deepcopy(estado_vecino)
    #estado_vecino = list(estado_vecino)
    #idx = range(len(estado_vecino))
    #i1, i2 = random.sample(idx, 2)
    #estado_vecino[i1], estado_vecino[i2] = estado_vecino[i2], estado_vecino[i1]
    # return list(estado_vecino)

    # Elijo aleatoriamente dos elementos de la lista
    producto_a = choice(lista_de_productos)
    producto_b = choice(lista_de_productos)
    # Creo una copia de la lista de productos que luego será el estado vecino
    estado_vecino = deepcopy(lista_de_productos)
    # Obtengo susrespectivos índices en la lista para asi poder intercambiarlos
    indice_a = estado_vecino.index(producto_a)
    indice_b = estado_vecino.index(producto_b)
    estado_vecino[indice_a], estado_vecino[indice_b] = estado_vecino[indice_b], estado_vecino[indice_a]
    if (producto_a == producto_b):
        # Si ambos coinciden se vuelve a generar el mismo vecino, entonces
        # se vuelve a llamar a la funcion estado_vecino_aleatorio; asi
        # intercambio de lugar dos ítems diferentes de la lista
        estado_vecino = estado_vecino_aleatorio(lista_de_productos)
    return (estado_vecino)


def distancia_recorrida(plano, lista_de_productos, df):
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
    matriz = deepcopy(plano)
    for i in range(len(posiciones) - 1):

        # IMPLEMENTACION CALCULANDO A* EN CADA ITERACION
        """  # Busco las coordenadas del elemento para poder buscarlo con A estrella
        matriz = deepcopy(plano)
        indices_a = ubicacion(matriz, posiciones[i])
        indices_b = ubicacion(matriz, posiciones[i + 1])
        # Sumo de todos los desplazamientos de ir de cada posicion a la proximo
        f_total = f_total + len(Astar(matriz, list(indices_a),list(indices_b ))) """

        # IMPLEMENTACION CON LAS DISTANCIAS YA CALCULADAS
        indices_a = ubicacion(matriz, posiciones[i])
        indices_b = ubicacion(matriz, posiciones[i + 1])
        indices_a = str(indices_a[0]) + " " + str(indices_a[1])
        indices_b = str(indices_b[0]) + " " + str(indices_b[1])
        costo = 0
        for i in range(0, len(df)):
            if ((df[i][0] == indices_a and df[i][1] == indices_b) or (df[i][0] == indices_b and df[i][1] == indices_a)):
                costo = int(df[i][2])
        f_total = f_total + costo

    return (f_total)


def recocido_simulado(plano, lista_de_productos, To=1000, alfa=0.9, Tf=0.05):
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
    # IMPLEMENTACION CON LAS DISTANCIAS YA CALCULADAS
    df = pd.read_csv('distancias.csv')
    df = df.to_numpy()

    
    e_actual = distancia_recorrida(plano, lista_de_productos, df)

    # Temperatura inicial
    T = To

    while (T >= Tf):
        # La Temperatura va disminuyendo a medida que avanza el algoritmo
        T = alfa * T

        # Intercambio de lugar dos ítems diferentes de la lista
        estado_vecino = estado_vecino_aleatorio(lista_de_productos)

        e_estado_vecino = distancia_recorrida(plano, estado_vecino, df)

        # La variación de energía dE es la función objetivo a minimizar
        dE = int(e_estado_vecino - e_actual)

        # Los movimientos que minimizan la distancia recorrida se aceptan siempre
        # Si el nuevo estado candidato es peor, podría llegar a aceptarse con
        # probabilidad pow(e, -dE/T)
        # if ((dE <= 0) or (probabilidad >= random())):
        # De no ser necesario calcular la probabilidad no se hace
        # nro_aleatorio = random.random()
        if ((dE <= 0) or (pow(e, -dE / T) >= random())):
            e_actual = e_estado_vecino
            lista_de_productos = estado_vecino

    # El algoritmo devuelve la mejor solución que se haya podido explorar y la
    # distancia minimiaza correspondiente
    dist_min = e_actual
    return (lista_de_productos, dist_min)
