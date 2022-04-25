import numpy as np

#================================== Algoritmo A* =========================================#
def Astar(matriz,inicio,destino):

    dim=len(matriz)
    flag=True
    actual=inicio                                                         

    Mfn=np.full((dim,dim),1000)                                          #Matriz que guardará las funciones f(n)
    caminos=np.full((dim,dim),None)                                      #Matriz que guardara los caminos hasta cada nodo

    caminos[actual[0]][actual[1]]=inicio

    matriz[actual[0]][actual[1]]='I'                                                      #Marcar inicio y fin del recorrido en el almacén
    matriz[destino[0]][destino[1]]='F'

    while(flag):
              
        for m in range(-1,2):
            for j in range(-1,2):
                if ((m==0 and j==-1)or(m==0 and j==1)or(j==0 and m==-1)or(j==0 and m==1)): #_Expando el nodo solo hacia arriba, abajo, der e iz
                    pSig=[actual[0]+m,actual[1]+j]                                         #_Posible posición siguiente. Dependendiendo de su f(n)

                    if pSig[0]>=0 and pSig[1]>=0 and pSig[0]<dim and pSig[1]<dim:          #_Que no se salga de los límites del almacén
                        if matriz[pSig[0]][pSig[1]]==0:                                    #_Para que avance solo por los pasillos                    
                            [f,hn]=fn(pSig,destino,len(caminos[actual[0]][actual[1]])-2)   #_Calculo f(n) de esa posición
                            Mfn[pSig[0]][pSig[1]]=f                                        #_Lo almaceno en la matriz

                            path=np.full(((len(caminos[actual[0]][actual[1]])+1)),None)
                            cont=0
                            for i in caminos[actual[0]][actual[1]]:
                                path[cont]=i
                                cont=cont+1
                            path[cont]=pSig
                            caminos[pSig[0]][pSig[1]]= path                                #Almaceno el camino hasta el nodo en cuestion
                            
                            if hn==1:                                                      #_Si estoy a un paso del destino se detiene
                                flag=False

        caminos[actual[0]][actual[1]]=None                        
        Mfn[actual[0]][actual[1]]=1000                                                    #_Reemplazo el valor de f(n) anterior para no volver a pasar por ese nodo        
        for i in range(0,dim):
            for j in range(0,dim):
                if (Mfn[i][j])==np.amin(Mfn):                                              #_Busco el nodo con el menor f(n)
                    actual=[i,j]


        matriz[actual[0]][actual[1]]='#'                                                  #_Marco el camino en el almacén
        cont=0

    path=path[2:len(path)]
    for i in path:
        matriz[i[0]][i[1]]='.'
    return path


#==================================== Calcular F(n)=h(n)+c(n)=============================#
def fn(pSig,destino,costo): 

    hn=abs(destino[0]-pSig[0])+abs(destino[1]-pSig[1])
    gn=costo
    fn=hn+gn
    return [fn,hn]