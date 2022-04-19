from Aestrella import *
import os

#====================== Armar la matriz que representa todo el almacen==================#
def almacen(matriz):
    PF=0             #Pasillo filas
    PC=0             #Pasillos columnas
    estante=0
    for i in range(0,10):
        matriz.append([0]*10)

    for i in range(0,10):
        for j in range(0,10):
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

#============================= Ubicar posiciones de destino =============================#
# Devuelve las coordenadas de la estantería que solicito
def ubicacion(matriz,pos):
    for i in range(0,10):
        for j in range(0,10):
            if matriz[i][j]==pos:
                pos=[i,j]
    return pos




#======================================== MAIN ===========================================#
if __name__=="__main__":
    
    matriz=[]
    matriz=almacen(matriz)                                                                #_Armo la matriz que representa al almacen
    print('\n')
    for i in range(0,10):                                                                 #_Graficar el almacén
        for j in range(0,10):
            print(matriz[i][j],end=' ')
        print('\n')

    inicio=[0,0]                                                                          #_Punto de partida
    pos1=ubicacion(matriz,int(input('Posición de destino: ')))                                     #_Saber el lugar de la matriz de la posicion de destino
    [matriz,camino]=Astar(matriz,inicio,pos1)                                               #_Encontramos el camino óptimo


    os.system('cls')
    print('Camino:\n',camino)
    print('Distancia recorrida: ',len(camino),' celdas')

    print('\n')
    for i in range(0,10):                                                                 #_Graficar el almacén y el recorrido
        for j in range(0,10):
            print(matriz[i][j],end=' ')
        print('\n')