from Aestrella import *
from numpy import *
import os
import pandas as pd

#====================== Armar la matriz que representa todo el almacen==================#
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

#============================= Ubicar posiciones de destino =============================#
# Devuelve las coordenadas de la estantería que solicito
def ubicacion(matriz,pos,dim):
    for i in range(0,dim):
        for j in range(0,dim):
            if matriz[i][j]==pos:
                pos=[i,j]
    return pos




#======================================== MAIN ===========================================#
if __name__=="__main__":
    
    matriz=[]
    print('\n')
    dim=16
    matriz=almacen(matriz,dim)                                                              #_Armo la matriz que representa al almacen
    print('\n')
    
    print(matrix(matriz))
    
    inicio=int(input('Posición de inicio: ') )                                                                                                                                              
    pos1=int(input('Posición de destino: ')   )                       #_Saber el lugar de la matriz de la posicion de destino
    #[matriz,camino]=Astar(matriz,inicio,pos1)                                               #_Encontramos el camino óptimo


    df=pd.read_csv('distancias.csv')
    df=df.to_numpy()

    for i in range(0,len(df)):
        if(df[i][0])==inicio and (df[i][1]==pos1):
            print(i)
            camino=df[i][2]



    #os.system('cls')

    print('Distancia recorrida: ',camino,' celdas')
