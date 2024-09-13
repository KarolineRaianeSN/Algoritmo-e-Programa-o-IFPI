import random
from functools import reduce

def range_nivel(nivel):
    if nivel == "1":
        minimo = 9
        maximo = 9
    elif nivel == "2":
        minimo = 4
        maximo = 6
    elif nivel == "3":
        minimo = 6
        maximo = 8
    return minimo, maximo

def preencher_torre(altura_minima, altura_maxima):
    rgb = ['R', 'G', 'B']
    # Gerar uma altura aleatória entre altura_minima e altura_maxima
    altura = random.randint(altura_minima, altura_maxima)
    # Retorna uma torre com altura definida e peças aleatórias de 'R', 'G', 'B'
    return [random.choice(rgb) for _ in range(altura)]

def iniciar_torres(nivel):
    # Pegar os valores de altura mínima e máxima para o nível fornecido
    altura_minima, altura_maxima = range_nivel(nivel)

    if nivel == "1":
        torre_R = preencher_torre(altura_minima, altura_maxima)
        torre_G = []
        torre_B = []
    elif nivel == "2":
        torre_R = preencher_torre(altura_minima, altura_maxima)
        torre_G = preencher_torre(altura_minima, altura_maxima)
        torre_B = preencher_torre(altura_minima, altura_maxima)
    elif nivel == "3":
        torre_R = preencher_torre(altura_minima, altura_maxima)
        torre_G = preencher_torre(altura_minima, altura_maxima)
        torre_B = preencher_torre(altura_minima, altura_maxima)

    return torre_R, torre_G, torre_B


def mover_item(torre_origem: list, torre_destino: list):
    if len(torre_destino) == 9:
        print("Impossível mover o item para uma torre cheia")
    torre_destino.append(torre_origem.pop())


def verificar_torre(torre: list, item: str) -> bool:
    return reduce(lambda acc, x: acc and (x == item), torre, True)
