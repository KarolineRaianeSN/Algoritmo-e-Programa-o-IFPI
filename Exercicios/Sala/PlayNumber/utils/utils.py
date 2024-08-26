import random
import os
import platform

def mostrar_menu():
    print("""
================== PLAYWORDS ===================
1  - Inicializar vetor
2  - Mostrar valores do vetor
3  - Resetar valor
4  - Exibir quantidade de itens do vetor
5  - Exibir maior e menor valor
6  - Somatório dos valores
7  - Média dos valores
8  - Mostrar positivos e quantidade deles
9  - Mostrar negativos e quantidade deles
10 - Atualizar todos os valores
11 - Adicionar novos valores
12 - Remover itens por valor exato
13 - Remover por posição
14 - Editar valor específico por posição
15 - Salvar valores em arquivo

0 - Sair""")


def menu_iniciar_vetor():
    limpar_tela()
    print("""
1 - Inserir números manualmente
2 - Inserir valores aleatorios no array
3 - Carregar valores a partir de um arquivo""")
    

def menu_atualizar_valores():
    limpar_tela()
    print("""
1. Multiplicar por um valor
2. Elevar a um valor (exponenciação)
3. Reduzir a uma fração
4. Substituir valores negativos por um número aleatório
5. Ordenar valores
6. Embaralhar valores""")

def pedir_numero(texto):
    return int(input(texto))


def pedir_numero_positivo(texto):
    numero = int(input(texto))
    while numero <= 0:
        print("Informe um número positivo.")
        numero = float(input(texto))
    return numero


def limpar_tela():
    sistema = platform.system()
    if sistema == "Windows":
        os.system('cls')
    else:  
        os.system('clear')
