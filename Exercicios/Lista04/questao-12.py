"""
. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
responda quem ganha a partida. A partida chega ao final se:
· Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
· Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma
diferença de 2 pontos sobre o adversário.
"""

def main():

    pontos_1 = 0
    pontos_2 = 0

    continua_partida = True

    while continua_partida:
        ganhador_ponto = int(input("Quem ganhou o ponto? (1 ou 2) "))
        if ganhador_ponto == 1:
            pontos_1 += 1
        else:
            pontos_2 += 1

        if pontos_1 == 21 or pontos_2 == 21:
            if pontos_1 - pontos_2 >= 2:
                continua_partida = False
            elif pontos_2 - pontos_1 >= 2:
                continua_partida = False





main()