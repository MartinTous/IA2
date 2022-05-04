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
from recocido_simulado import almacen, recocido_simulado
#from plyer import filechooser


if __name__ == "__main__":
    """ main:
    Punto de entrada donde se inicia el programa
    """

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
        nro_orden = int(input())
        ruta_txt_orden = "./ordenes/order_" + str(nro_orden) + ".txt"

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
    lista_ordenada, distancia_recorrida = recocido_simulado(
        matriz, lista_de_productos, To, alfa, Tf)
    print("Lista ordenada para reducir la distancia recorrida:")
    print(lista_ordenada)
    print("Distancia minimizada con la lista ordenada:", distancia_recorrida)
