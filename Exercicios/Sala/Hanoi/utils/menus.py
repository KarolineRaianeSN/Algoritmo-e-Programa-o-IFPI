import os
import platform
import random
from utils.manipulacao_torres import *

def como_jogar():
    print(f"""
----------------------------------------------------------------------------------
                                TORRE DE HANOI
----------------------------------------------------------------------------------

REGRAS: 
                        
-> O objetivo é colocar peças R na Torre R, G na Torre G e B na Torre B.

-> As torres funcionam como pilhas. Você só pode mover o topo de uma torre para outra.

-> Para mover, digite o par de torres. Exemplo:

    - "RG" move da Torre R para a Torre G.
    - O jogo acaba quando cada torre tiver apenas peças do seu tipo.


Nível 1: Todas as peças começam na Torre R.
Nível 2: Mais itens inicialmente espalhados nas Torres diversas e não só na primeira.
Nível 3: Tem o nível máximo de preenchimento inicial que permite ao usuário concluir o jogo.
Escolha entre 3 níveis de dificuldade: """)


def menu_inicial():
    texto_menu_inicial  = (f"""
----------------------------------------------------------------------------------
                                TORRE DE HANOI
----------------------------------------------------------------------------------

MENU INICIAL:

1. JOGAR
2. COMO JOGAR
0. SAIR
Escolha uma opção: """)

    return texto_menu_inicial

def menu_jogar():
    texto_menu_jogar = (f"""
----------------------------------------------------------------------------------
                                TORRE DE HANOI
----------------------------------------------------------------------------------


Nível 1: Todas as peças começam na Torre R.
Nível 2: Mais itens inicialmente espalhados nas Torres diversas e não só na primeira.
Nível 3: Tem o nível máximo de preenchimento inicial que permite ao usuário concluir o jogo.
0: Menu inicial
ESCOLHA UM NÍVEL: """)
    
    return input(texto_menu_jogar)


def exibir_torres(torre_R, torre_G, torre_B):
    altura_maxima = 9

    print("---------------------------")
    print("Torre R | Torre G | Torre B")
    print("---------------------------")
    

    for i in range(altura_maxima - 1, -1, -1):
        peca_R = torre_R[i] if i < len(torre_R) else ' '
        peca_G = torre_G[i] if i < len(torre_G) else ' '
        peca_B = torre_B[i] if i < len(torre_B) else ' '
        print(f"   {peca_R}    |    {peca_G}    |    {peca_B}   ")
    print("---------------------------")


def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:  
        os.system('clear')