#- Cabrero García, Gabriel
#- Mellimaci, Marcelo E
#- Tous Maggini, Martín

class ControladorDifuso:
    """ Clase PenduloInvertido
    
    Atributo:
        - self.reglas
    Metodos:
        - __init__
        - borrosificacion
        - cjto_difuso
        - control_difuso
        - desborrosificacion
    """    
    def __init__(self, reglas):
        """ Metodo __init__
        Metodo init o Constructor
        
        Parametro de Entrada:
            - reglas: diccionario con la tabla con las reglas de inferencia (FAM)
        Parametro de Salida:
            - Ninguno
        """ 
        
        #print("En el metodo __init__ de la clase ControladorDifuso")
        #print("reglas = ", reglas)
        
        # Tabla con las reglas de inferencia, eg:
        # self.reglas['NG']['PP'] es la Fza (borrosa) para theta NG y veloc PP
        self.reglas = reglas
        
    
    def borrosificacion(self, cjto_difuso, valor):
        """ Metodo borrosificacion
        Pasa a difuso el valor nítido de una entrada (borrosificador singleton)
        
        Parametros de Entrada:
            - cjto_difuso: lista con conjuntos borrosos de una variable de entrada
            - valor: valores de entrada nítidos (theta y omega)
        Parametro de Salida:
            - valores_difusos: valor de pertenencia dicha variable de entrada
        """          
        
        #print("En el metodo borrosificacion de la clase ControladorDifuso")
        #print("cjto_difuso = ", cjto_difuso)
        #print("valor = ", valor)
        
        # El parámetro "valor" se usará para los valores del omega y theta
        valores_difusos = {}
        for k in cjto_difuso[1]:
            valores_difusos[k] = cjto_difuso[1][k][cjto_difuso[0].searchsorted(valor)]
            
        #print("valores_difusos = ", valores_difusos)
        
        return (valores_difusos)
    
    
    def cjto_difuso(self, minimo, centro, maximo, variable_linguistica):
        """ Metodo cjto_difuso
        Genera una lista con los valores de pertenencia de dicho cjunto borroso
        
        Parametros de Entrada:
            - minimo: intersección izquierda del cjto difuso en el eje horizontal
            - centro: abscisa del punto de quiebre de la gráfica del cjto difuso
            - maximo: intersección derecha del cjto difuso en el eje de abscisas
            - variable_linguistica: array para el cjto borroso de la variable linguística
        Parametro de Salida:
            - cjto_borroso: lista con las sucesivas ordenadas del cjunto borroso
        """
        
        #print("En el metodo cjto_difuso de la clase ControladorDifuso")
        #print("minimo = ", minimo)
        #print("centro = ", centro)
        #print("maximo = ", maximo)
        #print("variable_linguistica = ", variable_linguistica)
        
        i_centro = variable_linguistica.searchsorted(centro)
        
        if (minimo != None):
            # Porcion lineal creciente
            cjto_a = i_centro * [0]
            i_minimo = variable_linguistica.searchsorted(minimo)
            for i in range(i_minimo, i_centro):
                cjto_a[i] = (i - i_minimo) / (i_centro - i_minimo)
        else:
            # Parte horizontal constante en 1 del cjto difuso mas a la izquierda
            cjto_a = i_centro * [1]
    
        if (maximo != None):
            # Funcn lineal decreciente
            cjto_b = (len(variable_linguistica) - i_centro) * [0]
            i_maximo = variable_linguistica.searchsorted(maximo)
            # Sumar 1 uno para que si tome el último valor del intervalo
            for i in range(i_centro, 1+i_maximo):
                cjto_b[i - i_centro] = - (i - i_centro) / (i_maximo - i_centro) + 1
        else:
             # Parte horizontal constante (en 1) del cjto difuso mas a la derecha
            cjto_b = (len(variable_linguistica) - i_centro) * [1]
            
        # Se unen las dos listas para asi formar el conjunto difuso
        cjto_borroso = cjto_a + cjto_b
        
        #print("cjto_borroso = ", cjto_borroso)
        
        return (cjto_borroso)
    
    
    def control_difuso(self, mu_fza, pendulo_angulo, pendulo_velocidad, mu_theta, mu_w):
        """ Metodo control_difuso
        Calcular la salida (F) en funcn de las entradas (theta y omega) mediante
        inferencia difusa
        
        Parametros de Entrada:
            - mu_fza: array con los conjuntos borrosos de la variable de salida
            - pendulo_angulo: valor numerico nitido de la posicion theta
            - pendulo_velocidad: valor numerico nitido de omega (theta_punto)
            - mu_theta: lista con los conjuntos borrosos de posicion angular
            - mu_w: lista con los conjuntos borrosos de velocidad angular
        Parametro de Salida:
            - F: Nro nítido de la variable Fza de salida (para el actuador)
        """
        
        #print("En el metodo control_difuso de la clase ControladorDifuso")
        #print("mu_fza = ", mu_fza)
        #print("pendulo_angulo = ", pendulo_angulo)
        #print("pendulo_velocidad = ", pendulo_velocidad)
        #print("mu_theta = ", mu_theta)
        #print("mu_w = ", mu_w)
        
        theta_difuso = self.borrosificacion(mu_theta, pendulo_angulo)
        omega_difuso = self.borrosificacion(mu_w, pendulo_velocidad)
    
        antecs = {
            'PG': 0,
            'PP': 0,
            'Z' : 0,
            'NP': 0,
            'NG': 0
        }
        for mu_theta in self.reglas.keys():
            for omega in self.reglas[mu_theta].keys():
                # Si alguno de los 2 valores de verdad es 0 nulo entonces no hace nada
                if ((theta_difuso[mu_theta] != 0) and (omega_difuso[omega] != 0)): 
                    antecedent_min = min(theta_difuso[mu_theta], omega_difuso[omega])
                    
                    # Obtengo el máximo de los mínimos (unión de intersecciones)
                    if (antecs[self.reglas[mu_theta][omega]] < antecedent_min):
                        antecs[self.reglas[mu_theta][omega]] = antecedent_min
                
        salida_borrosa = len(mu_fza[0]) * [0]
        # Cálculo de la salida borrosa (fuerza F)    
        for j in range(len(mu_fza[0])):
            for k in mu_fza[1].keys():
                fza_min = min(mu_fza[1][k][j], antecs[k])
                # Obtengo el máximo de los mínimos (unión de intersecciones)
                if (salida_borrosa[j] < fza_min):
                    salida_borrosa[j] = fza_min
    
        # Valor de Fza nitido
        F = self.desborrosificacion(mu_fza[0], salida_borrosa)
        
        #print("F = ", F)
        
        return (F)    
    
    
    def desborrosificacion(self, mu_fza, salida_borrosa):
        """ Metodo desborrosificacion
        Desborrosifica la variable de salida por Centroide o Ctro de Gravedad (COG)
        
        Parametros de Entrada:
            - mu_fza: arreglo con los conjuntos borrosos de la variable de salida
            - salida_borrosa: lista con el valor difuso para la variable de salida
        Parametro de Salida:
            - valor_nitido: Nro nítido de la variable de salida (para el actuador)
        """ 
        
        #print("En el metodo desborrosificacion de la clase ControladorDifuso")
        #print("mu_fza = ", mu_fza)
        #print("salida_borrosa = ", salida_borrosa)
        
        # Desborrosifica por Centroide o Ctro de Gravedad (Center Of Gravity COG)
        numerador = denominador = 0
        
        for y_c, mu in zip(mu_fza, salida_borrosa):
            #pdb.set_trace()
            numerador = numerador + y_c*mu
            denominador = denominador + mu
            
        valor_nitido = mu_fza[mu_fza.searchsorted(numerador/denominador)]
        
        #print("valor_nitido = ", valor_nitido)
        
        return (valor_nitido)