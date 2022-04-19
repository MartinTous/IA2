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

from numpy import array, genfromtxt, int32
from plyer import filechooser

from recocido_simulado import recocido_simulado


def main():
    """ Método main
    Punto de entrada donde se inicia el programa
    """
    print("\t Ejercicio 2 del TP 1 de IA 2 \n")

    plano = array([[0,  0,  0, 0, 0,  0,  0, 0],
                   [0,  1,  2, 0, 0, 25, 26, 0],
                   [0,  3,  4, 0, 0, 27, 28, 0],
                   [0,  5,  6, 0, 0, 29, 30, 0],
                   [0,  7,  8, 0, 0, 31, 32, 0],
                   [0,  0,  0, 0, 0, 0,   0, 0],
                   [0,  9, 10, 0, 0, 33, 34, 0],
                   [0, 11, 12, 0, 0, 35, 36, 0],
                   [0, 13, 14, 0, 0, 37, 38, 0],
                   [0, 15, 16, 0, 0, 39, 40, 0],
                   [0, 0,   0, 0, 0,  0,  0, 0],
                   [0, 17, 18, 0, 0, 41, 42, 0],
                   [0, 19, 20, 0, 0, 43, 44, 0],
                   [0, 21, 22, 0, 0, 45, 46, 0],
                   [0, 23, 24, 0, 0, 47, 48, 0],
                   [0,  0, 0,  0, 0,  0,  0, 0]])
    print("Mapa del almacen:")
    print(plano)
    
    # Lee la lista de picking de un archivo de texto indicado por el usuario
    print("Indique la ruta del archivo .txt con lista de productos de la orden ...")
    ruta_txt_orden = filechooser.open_file()[0]
    lista_de_productos = list(genfromtxt(ruta_txt_orden, dtype=int32))
    
    print("El archivo ingresado para tomar la lista de picking de la orden es:")
    print(ruta_txt_orden)
    print("Lista de picking sin ordenar:")
    print(lista_de_productos)
    
    To = 1000
    Tf = 0.05
    alfa = 0.9
    lista_ordenada, distancia_recorrida = recocido_simulado(To, alfa, Tf, plano, lista_de_productos)
    print("Lista ordenada para reducir la distancia recorrida:")
    print(lista_ordenada)
    print("Distancia minimizada con la lista ordenada:", distancia_recorrida)


if __name__ == "__main__":
    main()
