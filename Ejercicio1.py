#||============================================================================================||
#|| 1.Dado un almacén con un layout similar al siguiente, calcular el camino más corto (y la   ||
#||   distancia) entre 2 posiciones del almacén, dadas las coordenadas de estas posiciones,    ||
#||   utilizando el algoritmo A*                                                               ||
#||============================================================================================||

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

#=================== Algoritmo A* 
def Astar(matriz,actual,destino):
    fnMenor=1000
    while(actual!=destino):
        for i in range(-1,2):
            for j in range(-1,2):
                if i == 0 and j ==0:
                    pass
                else:
                    posSig=[actual[0]+i,actual[1]+j]
                    f=fn(posSig,destino,actual)
                    if f<fnMenor:
                        fnMenor=f
                        PS=posSig
        actual=PS
        matriz[PS[0]][PS[1]]='#'
    return matriz

#=============== Calcular F(n)=h(n)+c(n)===================#
def fn(posSig,pos1,posA): 
    hn=abs(pos1[0]-posSig[0])+abs(pos1[1]-posSig[1])
    gn=abs(posSig[0]-posA[0])+abs(posSig[1]-posA[1])
    fn=hn+gn
    return fn


#=============== MAIN ===================#
if __name__=="__main__":

    matriz=[]
    matriz=almacen(matriz)                                    #Armamos la matriz que representa al almacen

    pos0=[1,1]
    pos1=ubicacion(matriz,int(input('Posición 1: ')))        # Saber el lugar de la matriz de las posiciones de destino
    pos2=ubicacion(matriz,int(input('Posición 1: ')))   

    posA=pos0                                                # Partimos de las posición cero
    matriz=Astar(matriz,posA,pos1)                           # Encontramos el camino óptimo

    for i in range(0,10):
        print(matriz[i][:])

# final
