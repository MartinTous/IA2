""" _En este programa se calculan las distancias desde cada nodo de la matriz hasta el resto y se almacena
    _Unicamente es necesario correrlo en caso de que cambiemos la matriz que representa el almacen, 
     ya que el archivo csv que generamos queda guardado"""

from Aestrella import *
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


    # Este bloque se ejecuta en caso de que querramos volver a calcular 
    """ l=open("distancias.csv","w")
    l.write("inicio,destino,costo")
    for i in range(1,121):
        inicio=ubicacion(plano,i)
        print(i)
        for j in range(i+1,121):
            matriz= deepcopy(plano)
            destino=ubicacion(plano,j)
            [matriz,camino]=Astar(matriz,inicio,destino) 
            l.write(str(inicio)+","+str(destino)+","+str(len(camino))+"\n")
    l.close() """


    #df=pd.read_csv('distancias.csv')
    #df=df.to_numpy()



