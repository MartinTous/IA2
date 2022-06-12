#- Cabrero García, Gabriel
#- Mellimaci, Marcelo E
#- Tous Maggini, Martín
""" Ejercicio 3 del TP 2 de IA 2 / Año 2022 
Implementar un sistema de inferencia difusa para controlar un péndulo invertido
- Asuma que el carro no tiene espacio restringido para moverse
- Definir variables lingüísticas de entrada y salida, particiones borrosas, 
operaciones borrosas para la conjunción, disyunción e implicación, reglas de 
inferencia (cubrir todas las posibles combinaciones de valores borrosos de entrada
en la base de reglas)
- Utilice el modelo del sistema carro-péndulo en el Práctico Nº 2
"""

from numpy import arange, pi
import matplotlib.pyplot as plt
#import pdb

from controlador_difuso import ControladorDifuso
from pendulo_invertido import PenduloInvertido


def main():
    # Tabla con las reglas de inferencia, eg:
    # reglas['NG']['PP'] da la Fza (valor borroso) para theta NG y veloc PP
    reglas = {
        'PG': {'NG': 'Z',
               'NP': 'PP',
               'Z': 'PG',
               'PP': 'PG',
               'PG': 'PG'
               },
        'PP': {'NG': 'NP',
               'NP': 'Z',
               'Z': 'PP',
               'PP': 'PG',
               'PG': 'PG'
               },
        'Z': {'NG': 'NG',
              'NP': 'NP',
              'Z': 'Z',
              'PP': 'PP',
              'PG': 'PG'
              },
        'NP': {'NG': 'NG',
               'NP': 'NG',
               'Z': 'NP',
               'PP': 'Z',
               'PG': 'PP'
               },
        'NG': {'NG': 'NG',
               'NP': 'NG',
               'Z': 'NG',
               'PP': 'NP',
               'PG': 'Z'
               }
    }
    
    # ControladorDifuso(reglas)
    controlador_difuso = ControladorDifuso(reglas)
    
    # Paso para el tiempo y para crear los 3 tres cjtos difusos
    #paso = 0.05
    
    # Conjuntos borrosos para las entradas: mu_theta y mu_w

    # Conjuntos borrosos de la posición angular:
    paso_angulo = 0.001    # [rad]
    #paso_angulo = paso    # [rad]
    # Rango de -2*pi a 2*pi radianes
    mu_theta = [arange(-2 * pi, 2 * pi + paso_angulo, paso_angulo), {}]
    # arange(start, stop, step=..., dtype=..., *, like=...)  (de numpy)    
    mu_theta[1]['NG'] = controlador_difuso.cjto_difuso(None, -0.8, -0.5, mu_theta[0])
    mu_theta[1]['NP'] = controlador_difuso.cjto_difuso(-1, -0.5, 0, mu_theta[0])
    mu_theta[1]['Z'] = controlador_difuso.cjto_difuso(-0.5, 0, 0.5, mu_theta[0])
    mu_theta[1]['PP'] = controlador_difuso.cjto_difuso(0, 0.5, 1, mu_theta[0])
    mu_theta[1]['PG'] = controlador_difuso.cjto_difuso(0.5, 0.8, None, mu_theta[0])
    
    # Conjuntos borrosos de velocidad angular:
    paso_velocidad = 0.01      # [rad/s]
    #paso_velocidad = 0.005      # [rad/s]
    #paso_velocidad = paso      # [rad/s]
    mu_w = [arange(-15, 15+paso_velocidad, paso_velocidad), {}]
    mu_w[1]['NG'] = controlador_difuso.cjto_difuso(None, -9, -3.5, mu_w[0])
    mu_w[1]['NP'] = controlador_difuso.cjto_difuso(-6.5, -3.75, -1, mu_w[0])
    mu_w[1]['Z'] = controlador_difuso.cjto_difuso(-3, 0, 3, mu_w[0])
    mu_w[1]['PP'] = controlador_difuso.cjto_difuso(1, 3.75, 6.5, mu_w[0])
    mu_w[1]['PG'] = controlador_difuso.cjto_difuso(3.5, 9, None, mu_w[0])

    # Conjuntos borrosos para la salida: mu_fza
    # Conjuntos borrosos de fuerza
    #paso_fza = 0.05
    paso_fza = 0.1
    #paso_fza = paso
    mu_fza = [arange(-80, 80 + paso_fza, paso_fza), {}]
    mu_fza[1]['NG'] = controlador_difuso.cjto_difuso(None, -55, -30, mu_fza[0])
    mu_fza[1]['NP'] = controlador_difuso.cjto_difuso(-40, -20.25, 0.5, mu_fza[0])
    mu_fza[1]['Z'] = controlador_difuso.cjto_difuso(-15, 0, 15, mu_fza[0])
    mu_fza[1]['PP'] = controlador_difuso.cjto_difuso(0.5, 20.25, 40, mu_fza[0])
    mu_fza[1]['PG'] = controlador_difuso.cjto_difuso(30, 55, None, mu_fza[0])   
    
    # Gráficas de los conjuntos borrosos para theta, omega y Fza
    graficar_cjtos_difusos(mu_theta, 'Conjuntos borrosos de la posición angular', 'theta')
    graficar_cjtos_difusos(mu_w, 'Conjuntos borrosos de velocidad angular', 'omega')
    graficar_cjtos_difusos(mu_fza, 'Conjuntos borrosos de fuerza', 'Fza')
    
    # PenduloInvertido(l, m, M)
    pendulo = PenduloInvertido(0.5, 0.1, 1.0)
    
    # Listas que se usarán para graficar
    listado_theta = []
    listado_omega = []
    listado_alfa = []
    listado_fza = []
    listado_t = []
    # Parametros iniciales:
    angulo = pi/6  # Theta inicial [rad]
    velocidad = 0  # Omega inicial [rad / s]
    aceleracion = 0     # [rad / s**2]
    F = 0    
    t = 0
    # Para obtener buenos resultados tiene que ser <=0.02
    delta_t = 0.01
    #delta_t = paso
    tf = 10    
    while(t < tf):
        angulo, velocidad, aceleracion = pendulo.simular(angulo, velocidad, aceleracion, F, delta_t)
        F = controlador_difuso.control_difuso(mu_fza, angulo, velocidad, mu_theta, mu_w)

        listado_t.append(t)
        listado_theta.append(angulo)
        listado_omega.append(velocidad)
        listado_alfa.append(aceleracion)
        listado_fza.append(F)

        t = t + delta_t
    
    # Curvas de las respuestas de posición, velocidad angular, aceleración, y fzas
    graficar_curva(listado_t, listado_theta, 'theta', 'tiempo', 'Posición vs Tiempo')
    graficar_curva(listado_t, listado_omega, 'omega', 'tiempo', 'Velocidad vs Tiempo')
    graficar_curva(listado_t, listado_alfa, 'alfa', 'tiempo', 'Aceleración vs Tiempo')
    graficar_curva(listado_t, listado_fza, 'Fza', 'tiempo', 'Fuerza vs Tiempo')


def graficar_cjtos_difusos(mu, titulo, eje_x):
    plt.style.use('ggplot')
    
    nro_cjtos_difusos = 0
    for k in mu[1].values():
        nro_cjtos_difusos += 1
        plt.plot(mu[0], k)
        
    plt.xlabel(eje_x)
    plt.ylabel("Grado de Pertenencia (mu)")
    plt.title(titulo)
    if (nro_cjtos_difusos == 5):
        plt.text(0.5, 0.95, '(NG, NP, Z, PP, PG)',
                 horizontalalignment='center',
                 verticalalignment='center')
    
    plt.grid(True)
    plt.show() 
    
    
def graficar_curva(x, y, eje_x, eje_y, titulo):
    plt.style.use('ggplot')
    fig, ax = plt.subplots()
    ax.plot(x, y)
    
    ax.set_xlabel(eje_x)
    ax.set_ylabel(eje_y)
    ax.set_title(titulo)
    
    ax.grid(True)
    plt.show()


if __name__ == "__main__":
    main()