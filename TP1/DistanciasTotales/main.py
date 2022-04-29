from Aestrella import *
from numpy import *
import os
import pandas as pd
from copy import deepcopy


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
def ubicacion(matriz,pos):
    dim=len(matriz)
    for i in range(0,dim):
        for j in range(0,dim):
            if matriz[i][j]==pos:
                pos=[i,j]
    return pos




#======================================== MAIN ===========================================#
if __name__=="__main__":
    
    plano=[]
    print('\n')
    dim=16
    plano=almacen(plano,dim)                                                              #_Armo la matriz que representa al almacen
    print('\n')
    
    print(matrix(plano))

    l=open("distancias.csv","w")
    l.write("inicio,destino,costo")
    for i in range(1,121):
        inicio=ubicacion(plano,i)
        print(i)
        for j in range(i+1,121):
            matriz= deepcopy(plano)
            destino=ubicacion(plano,j)
            [matriz,camino]=Astar(matriz,inicio,destino) 
            l.write(str(inicio)+","+str(destino)+","+str(len(camino))+"\n")
    l.close()


    df=pd.read_csv('distancias.csv')
    df=df.to_numpy()

    for i in range(0,len(df)):
        if(df[i][0])==inicio and (df[i][1]==pos1):
            print(i)
            camino=df[i][2]



    #os.system('cls')

    print('Distancia recorrida: ',camino,' celdas')
