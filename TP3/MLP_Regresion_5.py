from ctypes import sizeof
import numpy as np
import matplotlib.pyplot as plt

# Generador basado en ejemplo del curso CS231 de Stanford: 
# CS231n Convolutional Neural Networks for Visual Recognition
# (https://cs231n.github.io/neural-networks-case-study/)
def generar_datos_clasificacion(cantidad_ejemplos,x1_neg_lim = -1,x1_pos_lim = 1,x2_neg_lim = -1,x2_pos_lim = 1,plot_data=1):
    """Receives x1 and x2 limits and generates a number of examples based in a sine cardinal function with noise 
    It plots the data if plot_data is True.

    Args:
        axis_lims (_float_): Limits of the working function
        number_of_examples (_int_): Number of examples to generate
        plot_data (_bool_): If True, plots the data
    
    Returns:
        x (_np array->3n x 2_): 2 Features
        y (_np array->3n x 1_): Function values

    """
    #Generate arrays of x1 and x2 that go from -14 to +14 with a step of 0.1
    x1_axis_values = np.arange(x1_neg_lim,x1_pos_lim,0.1)
    x2_axis_values = np.arange(x2_neg_lim,x2_pos_lim,0.1)

    x1_matrix = np.tile(x1_axis_values,(len(x2_axis_values),1))
    x1_matrix=x1_matrix.T
    #Create a matrix x2 with x2 as rows repeated according to size of x1
    x2_matrix = np.tile(x2_axis_values,(len(x1_axis_values),1))

    #Cardinal sine based function, with particular modifications
    y_matrix=-10*np.sin(np.sqrt(x1_matrix**2+x2_matrix**2))/np.sqrt(x1_matrix**2+x2_matrix**2)+50
    
    #Create a matrix of random gaussian numbers with the size of y and values between -1 and 1
    noise = np.random.normal(0,0.5,y_matrix.shape)
    y_matrix+=noise
    if plot_data:
        #Make a 3D plot of y_matrix 
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(x1_matrix,x2_matrix,y_matrix,cmap='viridis',edgecolor='none')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('y')
        ax.set_title('Original training function')
        plt.show()


    #Generate random examples based on the previous function
    #Generate number_of_examples random floats between x1_neg_lim and x1_pos_lim
    x1= np.random.uniform(x1_neg_lim,x1_pos_lim,cantidad_ejemplos)
    x2= np.random.uniform(x2_neg_lim,x2_pos_lim,cantidad_ejemplos)
    
    x= np.column_stack((x1,x2))
    y= -10*np.sin(np.sqrt(x1**2+x2**2))/np.sqrt(x1**2+x2**2)+50+np.random.normal(0,0.5,cantidad_ejemplos)
    
    if plot_data:
        #Plot the random generation of examples
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        #Plot the 3D plot of the points with x as axis and y as its value
        ax.scatter(x[:,0],x[:,1],y,c='r',marker='o')
        ax.set_xlabel('x1')
        ax.set_ylabel('x2')
        ax.set_zlabel('y')
        ax.set_title('Random generation of examples')
        plt.show()

    y=y.reshape(cantidad_ejemplos,1)
    YY=np.zeros(len(y), dtype = "uint8")
    for i in range (len(y)):
        YY[i] = y[i][0]
    return x,YY


def inicializar_pesos(n_entrada, n_capa_2, n_capa_3):
    randomgen = np.random.default_rng()

    w1 = 0.1 * randomgen.standard_normal((n_entrada, n_capa_2))
    b1 = 0.1 * randomgen.standard_normal((1, n_capa_2))

    w2 = 0.1 * randomgen.standard_normal((n_capa_2, n_capa_3))
    b2 = 0.1 * randomgen.standard_normal((1,n_capa_3))

    return {"w1": w1, "b1": b1, "w2": w2, "b2": b2}


def ejecutar_adelante(x, pesos):
    # Funcion de entrada (a.k.a. "regla de propagacion") para la primera capa oculta
    z = x.dot(pesos["w1"]) + pesos["b1"]
    # Funcion de activacion ReLU para la capa oculta (h -> "hidden")
    h = np.maximum(0, z)
    
    # Salida de la red (funcion de activacion lineal). Esto incluye la salida de todas
    # las neuronas y para todos los ejemplos proporcionados
    y = h.dot(pesos["w2"]) + pesos["b2"]
    
    return {"z": z, "h": h, "y": y}


def clasificar(x, pesos):
    # Corremos la red "hacia adelante"
    resultados_feed_forward = ejecutar_adelante(x, pesos)
    
    # Buscamos la(s) clase(s) con scores mas altos (en caso de que haya mas de una con 
    # el mismo score estas podrian ser varias). Dado que se puede ejecutar en batch (x 
    # podria contener varios ejemplos), buscamos los maximos a lo largo del axis=1 
    # (es decir, por filas)
    max_scores = np.argmax(resultados_feed_forward["y"], axis=1)

    # Tomamos el primero de los maximos (podria usarse otro criterio, como ser eleccion aleatoria)
    # Nuevamente, dado que max_scores puede contener varios renglones (uno por cada ejemplo),
    # retornamos la primera columna
    return max_scores[:]

# x: n entradas para cada uno de los m ejemplos(nxm)
# t: salida correcta (target) para cada uno de los m ejemplos (m x 1)
# pesos: pesos (W y b)
def train(x, t, pesos, learning_rate):
    # Cantidad de filas (i.e. cantidad de ejemplos)
    m = np.size(x, 0) 
    #epoch: Se cumple un epoch cuando se entrena la red neuronal con todos los ejemplos de entrenamiento una vez
    epoch=0
    pp=0
    while(pp==0):
        epoch += 1
        # Ejecucion de la red hacia adelante
        resultados_feed_forward = ejecutar_adelante(x, pesos)
        y = resultados_feed_forward["y"]
        h = resultados_feed_forward["h"]
        z = resultados_feed_forward["z"]
        
        # LOSS
        # a. Exponencial de todos los scores
        exp_scores = np.exp(y)
        
        # b. Suma de todos los exponenciales de los scores, fila por fila (ejemplo por ejemplo).
        #    Mantenemos las dimensiones (indicamos a NumPy que mantenga la segunda dimension del
        #    arreglo, aunque sea una sola columna, para permitir el broadcast correcto en operaciones
        #    subsiguientes)
        sum_exp_scores = np.sum(exp_scores, axis=1, keepdims=True)

        # c. "Probabilidades": normalizacion de las exponenciales del score de cada clase (dividiendo por 
        #    la suma de exponenciales de todos los scores), fila por fila
        p = exp_scores / sum_exp_scores
        
        # d. Calculo de la funcion de perdida global. Solo se usa la probabilidad de la clase correcta, 
        #    que tomamos del array t ("target")
        #loss = (1 / m) * np.sum( -np.log( p[range(m), t] ))
        mse = np.zeros((m,1))
        for k in range (m):
            mse[k] =(t[k]-y[k])
        loss = ( 1 / m ) *np.sum( pow( mse,2 ) ) 
        # Mostramos solo cada 1000 epochs
        if epoch %1000 == 0:
            print("Loss epoch", epoch, ":", loss)
        if epoch==10000:
            break

        # Extraemos los pesos a variables locales
        w1 = pesos["w1"]
        b1 = pesos["b1"]
        w2 = pesos["w2"]
        b2 = pesos["b2"]

        # Ajustamos los pesos: Backpropagation
        dL_dy = - 2 * mse / m                # Para todas las salidas, L' = p (la probabilidad)...

        dL_dw2 = h.T.dot(dL_dy)                         # Ajuste para w2
        dL_db2 = np.sum(dL_dy, axis=0, keepdims=True)   # Ajuste para b2

        dL_dh = dL_dy.dot(w2.T)
        
        dL_dz = dL_dh       # El calculo dL/dz = dL/dh * dh/dz. La funcion "h" es la funcion de activacion de la capa oculta,
        dL_dz[z <= 0] = 0   # para la que usamos ReLU. La derivada de la funcion ReLU: 1(z > 0) (0 en otro caso)

        dL_dw1 = x.T.dot(dL_dz)                         # Ajuste para w1
        dL_db1 = np.sum(dL_dz, axis=0, keepdims=True)   # Ajuste para b1

        # Aplicamos el ajuste a los pesos
        w1 += -learning_rate * dL_dw1
        b1 += -learning_rate * dL_db1
        w2 += -learning_rate * dL_dw2
        b2 += -learning_rate * dL_db2

        # Actualizamos la estructura de pesos
        # Extraemos los pesos a variables locales
        pesos["w1"] = w1
        pesos["b1"] = b1
        pesos["w2"] = w2
        pesos["b2"] = b2
        
    return pesos

def iniciar_training(numero_clases, numero_ejemplos,EPOCHS,LEARNING_RATE, graficar_datos):
    # Generamos datos
    x, t = generar_datos_clasificacion(numero_ejemplos)
    # Graficamos los datos si es necesario
    if graficar_datos:
        # Parametro: "c": color (un color distinto para cada clase en t)
        plt.scatter(x[:, 0], x[:, 1], c=t)
        plt.show()

    # Inicializa pesos de la red
    NEURONAS_CAPA_OCULTA = 100
    NEURONAS_ENTRADA = 2
    pesos = inicializar_pesos(n_entrada=NEURONAS_ENTRADA, n_capa_2=NEURONAS_CAPA_OCULTA, n_capa_3=1)
    # Entrena
    LEARNING_RATE=0.01
    pesos=train(x, t, pesos, LEARNING_RATE)
    return pesos,x,t



#COMENZAMOS ENTRENANDO LA RED NEURONAL
print("\nEntrenando la red neuronal...\n")
EPOCHS=100000
LEARNING_RATE=0.01
pesos,x,t=iniciar_training(numero_clases=3, numero_ejemplos=300, EPOCHS=1000,LEARNING_RATE=1,graficar_datos=False)


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Plot the 3D plot of the points with x as axis and y as its value
ax.scatter(x[:,0],x[:,1],t,cmap='viridis',edgecolor='none')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.set_title('Random generation of examples')
plt.show()


