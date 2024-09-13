from random import *
from utils.jogo import *
from utils.manipulacao_torres import *
from utils.menus import *

def main():
    opcao = input(menu_inicial())
    limpar_tela()

    while opcao != "0":
        if opcao == "1":  # JOGAR
            torre_R, torre_G, torre_B = iniciar_torres(menu_jogar())
            exibir_torres(torre_R, torre_G, torre_B)

            jogador_um = jogo()
            jogador_dois = jogo()

            # quem ganhou




        elif opcao == "2":  # COMO JOGAR
            como_jogar()

        input("Aperte enter para voltar...")
        limpar_tela()
        opcao = input(menu_inicial())


main()