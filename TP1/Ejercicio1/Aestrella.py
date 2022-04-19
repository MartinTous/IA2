import numpy as np


#================================== Algoritmo A* =========================================#
def Astar(matriz,inicio,destino):
    dim=10
    flag=True
    actual=inicio
    Mfn=[]                                                                                #Matriz que guardará las funciones f(n)
    costo=[]                                                                              #Matriz que guardará el costo c(n)
    caminos=[]                                                                            #Matriz que guardara los caminos hasta cada nodo

    for i in range(0,10):
        Mfn.append([10000]*dim)
        caminos.append([0]*10)

    caminos[actual[0]][actual[1]]=[0,0]

    matriz[actual[0]][actual[1]]='I'                                                      #Marcar inicio y fin del recorrido en el almacén
    matriz[destino[0]][destino[1]]='F'

    while(flag):
        costo.append(1) 
           
        for i in range(-1,2):
            for j in range(-1,2):
                if ((i==0 and j==-1)or(i==0 and j==1)or(j==0 and i==-1)or(j==0 and i==1)): #_Expando el nodo solo hacia arriba, abajo, der e iz
                    pSig=[actual[0]+i,actual[1]+j]                                         #_Posible posición siguiente. Dependendiendo de su f(n)
                    if pSig[0]>=0 and pSig[1]>=0 and pSig[0]<dim and pSig[1]<dim:          #_Que no se salga de los límites del almacén
                        if matriz[pSig[0]][pSig[1]]==0:                                    #_Para que avance solo por los pasillos                        
                            [f,hn]=fn(pSig,destino,costo)                                  #_Calculo f(n) de esa posición
                            Mfn[pSig[0]][pSig[1]]=f                                        #_Lo almaceno en la matriz
                            
                            path=[]
                            path.append(caminos[actual[0]][actual[1]])
                            path.append(pSig)
                            caminos[pSig[0]][pSig[1]]= path                                #Almaceno el camino hasta el nodo en cuestion
                            if hn==1:                                                      #_Si estoy a un paso del destino se detiene
                                flag=False
                                
     
        Mfn[actual[0]][actual[1]]=10000                                                    #_Reemplazo el valor de f(n) anterior para no volver a pasar por ese nodo        
        for i in range(0,dim):
            for j in range(0,dim):
                if (Mfn[i][j])==np.amin(Mfn):                                              #_Busco el nodo con el menor f(n)
                    actual=[i,j]

       
        matriz[actual[0]][actual[1]]='#'                                                   #_Marco el camino en el almacén

    return [matriz,path]


#==================================== Calcular F(n)=h(n)+c(n)=============================#
def fn(pSig,destino,costo): 

    hn=abs(destino[0]-pSig[0])+abs(destino[1]-pSig[1])
    gn=sum(costo)
    fn=hn+gn
    return [fn,hn]