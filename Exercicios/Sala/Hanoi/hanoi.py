from random import *
from utils.jogo import *
from utils.manipulacao_torres import *
from utils.menus import *

def main():
    opcao = input(menu_inicial())
    limpar_tela()

    while opcao != "0":
        if opcao == "1":  # JOGAR
            jogadores = {}

            qtd_jogadores = int(input("Numero de jogadores: "))
            limpar_tela()
            torre_R, torre_G, torre_B = iniciar_torres(menu_jogar())

            for index_jogador in range(0, qtd_jogadores):
                limpar_tela()
                nome_jogador = input(f"Jogador {index_jogador + 1}: ")
                jogadas = jogo(torre_R, torre_G, torre_B)

                jogadores.update({nome_jogador: jogadas})

                print(f"{nome_jogador} fez {jogadas} jogadas")
            limpar_tela()
            mostrar_placar(jogadores)

        elif opcao == "2":  # COMO JOGAR
            como_jogar()

        input("Aperte enter para voltar...")
        limpar_tela()
        opcao = input(menu_inicial())


main()