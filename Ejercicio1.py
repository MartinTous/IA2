#||============================================================================================||
#|| 1.Dado un almacén con un layout similar al siguiente, calcular el camino más corto (y la   ||
#||   distancia) entre 2 posiciones del almacén, dadas las coordenadas de estas posiciones,    ||
#||   utilizando el algoritmo A*                                                               ||
#||============================================================================================||
import numpy as np
#====== Armar la matriz que representa todo el almacen=====#
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

#============ Ubicar posiciones de destino ================#
def ubicacion(matriz,pos):
    for i in range(0,10):
        for j in range(0,10):
            if matriz[i][j]==pos:
                pos=[i,j]
    return pos

#=================== Algoritmo A* =========================#
def Astar(matriz,actual,destino):
    dim=10
    flag=True

    Mfn=[]
    for i in range(0,dim):
        Mfn.append([10000]*dim)

    matriz[actual[0]][actual[1]]='I'
    matriz[destino[0]][destino[1]]='F'
    while(flag):
        for i in range(-1,2):
            for j in range(-1,2):
                if ((i==0 and j==-1)or(i==0 and j==1)or(j==0 and i==-1)or(j==0 and i==1)):
                    pSig=[actual[0]+i,actual[1]+j]
                    if pSig[0]>=0 and pSig[1]>=0 and pSig[0]<dim and pSig[1]<dim:
                        if matriz[pSig[0]][pSig[1]]==0:
                            f=fn(pSig,destino,actual)
                            Mfn[pSig[0]][pSig[1]]=f
                            if f==2:
                                flag=False

        Mfn[actual[0]][actual[1]]=10000                 
        for i in range(0,dim):
            for j in range(0,dim):
                if (Mfn[i][j])==np.amin(Mfn):
                    actual=[i,j]
           
        matriz[actual[0]][actual[1]]='#' 
   
    return matriz

#=============== Calcular F(n)=h(n)+c(n)===================#
def fn(pSig,destino,Actual): 
    hn=abs(destino[0]-pSig[0])+abs(destino[1]-pSig[1])
    gn=abs(pSig[0]-Actual[0])+abs(pSig[1]-Actual[1])
    fn=hn+gn
    return fn


#=============== MAIN ===================#
if __name__=="__main__":

    matriz=[]
    matriz=almacen(matriz)                                    #Armamos la matriz que representa al almacen

    pos0=[0,0]
    pos1=ubicacion(matriz,int(input('Posición 1: ')))        # Saber el lugar de la matriz de las posiciones de destino
  

    posA=pos0                                                # Partimos de las posición cero
    matriz=Astar(matriz,posA,pos1)                           # Encontramos el camino óptimo
    
    print('\n')
    for i in range(0,10):
        for j in range(0,10):
            print(matriz[i][j],end=' ')
        print('\n')