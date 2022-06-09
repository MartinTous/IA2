#- Cabrero García, Gabriel
#- Mellimaci, Marcelo E
#- Tous Maggini, Martín

from scipy import constants
from math import sin, cos

class PenduloInvertido:
    def __init__(self, l, m, M):
        self.long_pendulo = l         # [m]
        self.masa_pendulo = m         # [Kg]
        self.masa_carro = M           # [Kg]
        
    def simular(self, angulo, velocidad, aceleracion, fuerza, delta_t):
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