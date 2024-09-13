import random

def preencher_torre(altura):
    rgb = ['R', 'G', 'B']
    return [random.choice(rgb) for _ in range(random.randrange(0, altura))]


def iniciar_torres(nivel):
    altura_maxima = 9
    if nivel == "1":
        torre_R = preencher_torre(altura_maxima)
        torre_G = []
        torre_B = []
    elif nivel == "2":
        torre_R = preencher_torre(altura_maxima/2)
        torre_G = preencher_torre(altura_maxima/2)
        torre_B = preencher_torre(altura_maxima/2)
    elif nivel == "3":
        torre_R = preencher_torre(altura_maxima)
        torre_G = preencher_torre(altura_maxima)
        torre_B = preencher_torre(altura_maxima)
    return torre_R, torre_G, torre_B


def mover_item(torre_origem, torre_destino):
    if len(torre_destino) == 9:
        print("Impossível mover o item para uma torre cheia")
    torre_destino.append(torre_origem.pop())


def verificar_torre(torre: list, item: str) -> bool:
    return all(map(torre, lambda x: x == item))
