#- Cabrero García, Gabriel
#- Mellimaci, Marcelo E
#- Tous Maggini, Martín

from scipy import constants
from math import sin, cos

class PenduloInvertido:
    """ Clase PenduloInvertido
    
    Atributos:
        - self.long_pendulo
        - self.masa_pendulo
        - self.masa_carro
    Metodos:
        - __init__
        - simular
    """ 
    
    def __init__(self, l, m, M):
        """ Metodo __init__
        Metodo init o Constructor
        
        Parametros de Entrada:
            - l: longitud de la barra del péndulo [m]
            - m: masa del péndulo (pertiga) [Kg]
            - M: Masa del carro [Kg]
        Parametro de Salida:
            - Ninguno
        """        
        self.long_pendulo = l         # [m]
        self.masa_pendulo = m         # [Kg]
        self.masa_carro = M           # [Kg]
        
    def simular(self, angulo, velocidad, aceleracion, fuerza, delta_t):
        """ Método simular
        Modelo del sistema carro-péndulo invertido
        
        Parametros de Entrada:
            - angulo: Posición angular (theta) inicial [rad]
            - velocidad: Velocidad angular (omega) inicial [rad / s]
            - aceleracion: Aceleración angular (alfa) inicial [rad / s**2]
            - fuerza: Fuerza horizonal ejercida en el carro
            - delta_t: incremento de tiempo por iteracion (paso)
        Parametros de Salida:
            - angulo: Posición angular (theta) final [rad]
            - velocidad: Velocidad angular (omega) final [rad / s]
            - aceleracion: Aceleración angular (alfa) final [rad / s**2]
        """        
        l = self.long_pendulo
        m = self.masa_pendulo
        M = self.masa_carro
        
        # Aceleración angular (theta_dos_puntos)
        numerador = (constants.g * sin(angulo) 
                     + cos(angulo)*(-fuerza-m*l*pow(velocidad,2)*sin(angulo))/(M+m))
        denominador = l * (4/3 - m*pow(cos(angulo),2)/(M+m))
        aceleracion = numerador / denominador
        
        # Velocidad angular (theta_punto)
        velocidad = velocidad + aceleracion*delta_t
        
        # Ángulo de la posición del péndulo (theta)
        angulo = (angulo 
                  + velocidad*delta_t 
                  + aceleracion*pow(delta_t, 2)/2)
        
        return (angulo, velocidad, aceleracion)