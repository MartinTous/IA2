#- Cabrero García, Gabriel
#- Mellimaci, Marcelo E
#- Tous Maggini, Martín

class ControladorDifuso:
    def __init__(self, reglas):
        # Tabla con las reglas de inferencia, eg:
        # self.reglas['NG']['PP'] es la Fza (borrosa) para theta NG y veloc PP
        self.reglas = reglas
        
    
    def borrosificacion(self, cjto_difuso, valor):
        # El parámetro "valor" se usará para los valores del omega y theta
        valores_difusos = {}
        for k in cjto_difuso[1]:
            valores_difusos[k] = cjto_difuso[1][k][cjto_difuso[0].searchsorted(valor)]
        return (valores_difusos)
    
    
    def cjto_difuso(self, minimo, centro, maximo, variable_linguistica):
        i_centro = variable_linguistica.searchsorted(centro)
        
        if (minimo != None):
            cjto_a = i_centro * [0]
            i_minimo = variable_linguistica.searchsorted(minimo)
            for i in range(i_minimo, i_centro):
                cjto_a[i] = (i - i_minimo) / (i_centro - i_minimo)
        else:
            cjto_a = i_centro * [1]
    
        if (maximo != None):
            cjto_b = (len(variable_linguistica) - i_centro) * [0]
            i_maximo = variable_linguistica.searchsorted(maximo)
            # Sumar 1 uno para que si tome el último valor del intervalo
            for i in range(i_centro, 1+i_maximo):
                cjto_b[i - i_centro] = - (i - i_centro) / (i_maximo - i_centro) + 1
        else:
            cjto_b = (len(variable_linguistica) - i_centro) * [1]
            
        cjto_borroso = cjto_a + cjto_b
        return (cjto_borroso)
    
    
    def control_difuso(self, mu_fza, pendulo_angulo, pendulo_velocidad, mu_theta, mu_w):
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
                
        F_nitido = len(mu_fza[0]) * [0]
        # Cálculo de la salida borrosa (fuerza F)    
        for j in range(len(mu_fza[0])):
            for k in mu_fza[1].keys():
                fza_min = min(mu_fza[1][k][j], antecs[k])
                # Obtengo el máximo de los mínimos (unión de intersecciones)
                if (F_nitido[j] < fza_min):
                    F_nitido[j] = fza_min
    
        # Valor de Fza nitido
        F = self.desborrosificacion(mu_fza[0], F_nitido)
        return (F)    
    
    
    def desborrosificacion(self, mu_fza, F_nitido):
        # Desborrosifica por Centroide o Ctro de Gravedad (Center Of Gravity COG)
        numerador = denominador = 0
        
        for y_c, mu in zip(mu_fza, F_nitido):
            #pdb.set_trace()
            numerador = numerador + y_c*mu
            denominador = denominador + mu
            
        valor_nitido = mu_fza[mu_fza.searchsorted(numerador/denominador)]
        return (valor_nitido)