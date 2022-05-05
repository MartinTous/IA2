""" Ejercicio 2 del TP 1 de IA 2 / Año 2022
- Cabrero García, Gabriel
- Mellimaci, Marcelo E
- Tous Maggini, Martín
OBTENCIÓN DEL ORDEN OPTIMO DE PICKING MEDIANTE RECOCIDO SIMULADO:
Dada una orden de pedido, que incluye una lista de productos del 
almacén anterior que deben ser despachados en su totalidad, determinar el 
orden óptimo para la operación de picking mediante Temple Simulado. ¿Qué 
otros algoritmos pueden utilizarse para esta tarea?
"""
# TODO: Probar si se puede mejorar usando dos veces el recocido simulado, de forma
# tal que la salida de un recocido simulado sea la entrada del segundo

from numpy import array, genfromtxt, int32, matrix
from recocido_simulado import RecocidoSimulado
import os.path


def almacen(matriz, dim):
    """ Función almacen
    Genera una matriz cuadrada con los elementos del plano del almacén
    Parametros de Entrada:
        matriz: Lista [] para colocar matriz cuadrada con el plano del almacén
        dim: Dimensiones de la matriz cuadrada
    Parametro de Salida:
        matriz: Matriz cuadrada con los elementos del almacén
    """
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


if __name__ == "__main__":
    """ main:
    Punto de entrada donde se inicia el programa
    """
    
    recocido_simulado = RecocidoSimulado()
    
    print("\t Ejercicio 2 del TP 1 de IA 2")

    matriz = []
    print('\n')
    #dim=int(input('Tamaño del almacen (LxL) -> L= '))
    dim = 16
    matriz = almacen(matriz, dim)
    print(matrix(matriz))

    # Lee la lista de picking de un archivo de texto indicado por el usuario
    try:
        print("Indique el nro [1 ; 100] de la orden: ")
        nro_order = int(input())
        order = "order_" + str(nro_order) + ".txt"
        # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f
        ruta_txt_orden = os.path.join("ordenes", order)
        # /home/marceemellimaci/Documents/2022/ia2/Practica-IA2/TP1/Ejercicio2/ordenes/order_1.txt
        lista_de_productos = list(genfromtxt(ruta_txt_orden, dtype=int32))

    except:
        print("Error cargando el archivo .txt con lista de productos de la orden !")
        # exit()

    print("El archivo ingresado para tomar la lista de picking de la orden es:")
    print(ruta_txt_orden)

    print("Lista de picking sin ordenar:")
    print(lista_de_productos)

    To = 1000
    Tf = 0.05
    alfa = 0.9
    lista_ordenada, distancia_recorrida = recocido_simulado.optimizar(
        matriz, lista_de_productos, To, alfa, Tf)
    print("Lista ordenada para reducir la distancia recorrida:")
    print(lista_ordenada)
    print("Distancia minimizada con la lista ordenada:", distancia_recorrida)
