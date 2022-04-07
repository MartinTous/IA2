from turtle import goto
import numpy as np
from cmath import sqrt


#=========CALCULO DE EURISTICA==========
def dist(x,y,xf,yf):
    a = abs(xf-x) + abs(yf-y)
    return a 
#=======================================


#=============CREAR GRILLA==============
def almacen(entradax,entraday,salidax,saliday):
    matriz = []
    for i in range(0,10):
        matriz.append([0]*10)

    for i in range(0,10):
        for j in range(0,10):
            if i == entradax and j == entraday:
                matriz[i][j] = 1 
            elif i == salidax and j == saliday:
                matriz[i][j] = 1 
            else:      
                matriz[i][j] = 0 
    return (matriz)
    #for i in range(10):
        #print('\n',matriz[i])
#=======================================

#=============ALGORITMO A*==============
if __name__=="__main__":
    #====DEFINIR PUNTO INICIAL Y FINAL======
    entradax =0 #int (input('Ingrese coordenada x de entrada--> '))
    entraday =0 #int (input('Ingrese coordenada y de entrada--> '))
    salidax =6 #int (input('Ingrese coordenada x de salida--> '))
    saliday =4 #int (input('Ingrese coordenada y de salida--> '))
    #=======================================
    xa = entradax
    ya = entraday

    F = []
    for i in range(0,10):
        F.append([0]*10)

    for i in range(0,10):
        for j in range(0,10):      
                F[i][j] = 10000 
    g = 1
    flag = True
    k = 0 
    matriz = almacen(entradax,entraday,salidax,saliday)
    while(flag):
        k += 1
        #print(k)

        if ya != 0:
            #ARRIBA
            F [xa][ya-1] = dist(xa,ya-1,salidax,saliday) + dist(xa,ya,xa,ya-1)

        if ya != 0 and xa != 9:
            #ARRIBA DERECHA
            F [xa+1][ya-1] = dist(xa+1,ya-1,salidax,saliday) + dist(xa,ya,xa+1,ya-1)  

        if ya != 0 and xa != 0:
            #ARRIBA IZQUIERDA
            F [xa - 1][ya - 1] = dist(xa - 1,ya - 1,salidax,saliday) + dist(xa,ya,xa - 1,ya - 1)  

        if ya != 9:
            #ABAJO
            F [xa][ya + 1] = dist(xa,ya + 1,salidax,saliday) + dist(xa,ya,xa,ya + 1)

        if ya != 9 and xa != 9:
            #ABAJO DERECHA
            F [xa + 1][ya + 1] = dist(xa + 1,ya + 1,salidax,saliday) + dist(xa,ya,xa + 1,ya + 1)  

        if ya != 9 and xa != 0:
            #ABAJO IZQUIERDA
            F [xa - 1][ya + 1] = dist(xa - 1,ya + 1,salidax,saliday) + dist(xa,ya,xa - 1,ya + 1)  

        if xa != 9:
            #DERECHA
            F [xa + 1][ya] = dist(xa + 1,ya,salidax,saliday) + dist(xa,ya,xa + 1,ya)

        if xa != 0:
            #IZQUIERDA
            F [xa - 1][ya] = dist(xa - 1,ya,salidax,saliday) + dist(xa,ya,xa - 1,ya)

        pp = True
        for i in range(0,10):
            for j in range(0,10):      
                    if F[i][j] == np.amin(F):
                        xa = i
                        ya = j
                        matriz[xa][ya] = 7
                        pp = False
                        break 
            if pp == False:
                break
        

        if xa == salidax and ya == saliday:
            flag = False
            print('LLEGUE')
    #=======================================


print('\n\n\n')
for i in range(10):
    print('\n',matriz[i])











