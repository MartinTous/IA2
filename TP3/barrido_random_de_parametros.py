#Se obtuvieron 15 combinaciones distintas de valores de ritmo de aprendizaje (entre
#cero y uno) y cantidad de neuronas (entre 1 y 1000) en la capa oculta de la red neuronal
import random

def main():
    for i in range(15):
        epsilon_y_cantdad_de_neuronas_random()


def epsilon_y_cantdad_de_neuronas_random():
    print("\nlearning_rate =", random.random())
    print("neuronas_capa_oculta =", random.randint(1, 1001))


if __name__ == '__main__':
    main()