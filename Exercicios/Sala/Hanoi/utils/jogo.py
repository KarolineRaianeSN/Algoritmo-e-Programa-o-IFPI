from utils.manipulacao_torres import mover_item, verificar_torre
from utils.menus import *


def jogada():
    torres = list(input("Torre origem e destino (ex: 'rg'): "))

    input_torre_origem = torres[0].upper()
    input_torre_destino = torres[1].upper()

    if input_torre_origem == input_torre_destino:
        print("Jogada invalida. Torre origem e destino devem ser diferentes.")
        return jogada()

    if input_torre_origem not in ["R", "G", "B"] or input_torre_destino not in ["R", "G", "B"]:
        print("Jogada invalida. Torre origem e destino devem ser R, G ou B.")
        return jogada()

    return input_torre_origem, input_torre_destino


def jogo_finalizado(torre_R, torre_G, torre_B):
    return verificar_torre(torre_R, 'R') and verificar_torre(torre_G, 'G') and verificar_torre(torre_B, 'B')


def mostrar_placar(jogadores):
    vencedor = max(jogadores, key=jogadores.get)
    
    for jogador, jogadas in jogadores.items():
        print(f"{jogador}: {jogadas} jogadas")
    limpar_tela()
    print(f"VENCEDOR: {vencedor}")


def jogo(torre_R, torre_G, torre_B):
    torres = {
        'R': torre_R.copy(),
        'G': torre_G.copy(),
        'B': torre_B.copy()
    }

    contador_jogadas = 0

    while not jogo_finalizado(torres['R'], torres['G'], torres['B']):
        exibir_torres(torres['R'], torres['G'], torres['B'])
        print(f"Jogadas: {contador_jogadas} jogadas")

        index_origem, index_destino = jogada()

        mover_item(torres[index_origem], torres[index_destino])

        contador_jogadas += 1

        limpar_tela()
    
    print(f"Jogo finalizado em {contador_jogadas} jogadas")

    return contador_jogadas
