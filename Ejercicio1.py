
import numpy as np
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

#================================== Algoritmo A* =========================================#
def Astar(matriz,actual,destino):
    dim=10
    flag=True

    Mfn=[]                                                                                 #Matriz que guardará las funciones f(n)
    for i in range(0,dim):
        Mfn.append([10000]*dim)

    matriz[actual[0]][actual[1]]='I'                                                       #Marcar inicio y fin del recorrido en el almacén
    matriz[destino[0]][destino[1]]='F'
    while(flag):
        for i in range(-1,2):
            for j in range(-1,2):
                if ((i==0 and j==-1)or(i==0 and j==1)or(j==0 and i==-1)or(j==0 and i==1)): #_Expando el nodo solo hacia arriba, abajo, der e iz
                    pSig=[actual[0]+i,actual[1]+j]                                         #_Posible posición siguiente. Dependendiendo de su f(n)
                    if pSig[0]>=0 and pSig[1]>=0 and pSig[0]<dim and pSig[1]<dim:          #_Que no se salga de los límites del almacén
                        if matriz[pSig[0]][pSig[1]]==0:                                    #_Para que avance solo por los pasillos
                            f=fn(pSig,destino,actual)                                      #_Calculo f(n) de esa posición
                            Mfn[pSig[0]][pSig[1]]=f                                        #_Lo almaceno
                            if f==2:                                                       #_Si estoy a un paso del destino se detiene
                                flag=False

        Mfn[actual[0]][actual[1]]=10000                                                    #_Reemplazo el valor de f(n) anterior para no volver a pasar por ese nodo        
        for i in range(0,dim):
            for j in range(0,dim):
                if (Mfn[i][j])==np.amin(Mfn):                                              #_Busco el nodo con el menor f(n)
                    actual=[i,j]
           
        matriz[actual[0]][actual[1]]='#'                                                   #Marco el camino en el almacén
   
    return matriz

#==================================== Calcular F(n)=h(n)+c(n)=============================#
def fn(pSig,destino,Actual): 
    hn=abs(destino[0]-pSig[0])+abs(destino[1]-pSig[1])
    gn=abs(pSig[0]-Actual[0])+abs(pSig[1]-Actual[1])
    fn=hn+gn
    return fn


#======================================== MAIN ===========================================#
if __name__=="__main__":

    matriz=[]
    matriz=almacen(matriz)                                                                #_Armo la matriz que representa al almacen
    print('\n')
    for i in range(0,10):                                                                 #_Graficar el almacén y el recorrido
        for j in range(0,10):
            print(matriz[i][j],end=' ')
        print('\n')

    pos0=[0,0]                                                                            #_Punto de partida
    pos1=ubicacion(matriz,int(input('Posición 1: ')))                                     #_Saber el lugar de la matriz de las posiciones de destino
  
    posA=pos0                                                                             #_Partimos de las posición cero
    matriz=Astar(matriz,posA,pos1)                                                        #_Encontramos el camino óptimo

    os.system('cls')
    print('\n')
    for i in range(0,10):                                                                 #_Graficar el almacén y el recorrido
        for j in range(0,10):
            print(matriz[i][j],end=' ')
        print('\n')