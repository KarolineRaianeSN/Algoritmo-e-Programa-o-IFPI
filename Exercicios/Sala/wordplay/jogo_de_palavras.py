""" 
Leitura de lista de palavras
1 - Ler e imprimir apenas as palavras com mais de 20 caracteres
2 - Escrever uma função "has_no_e" que retorne True se a palavra não tiver a letra "e"
3 - Escreva uma função chamada avoids que receba uma palavra e uma série de letras proibidas, e retorne True se a palavra não usar nenhuma das letras proibidas, além disso o usuário pode digitar uma série de letras proibidas e o programa imprimirá o número de palavras que não contém nenhuma delas
4 - Escreva uma função chamada uses_only que receba uma palavra e uma série de letras e retorne True, se a palavra só contiver letras da lista. 
5 - Escreva uma função chamada uses_all que receba uma palavra e uma série de letras obrigatórias e retorne True se a palavra usar todas as letras obrigatórias pelo menos uma vez.
6 - Escreva uma função chamada is_abecedarian que retorne True se as letras numa palavra aparecerem em ordem alfabética (tudo bem se houver letras duplas). Quantas palavras em ordem alfabética existem?
"""
import os

def main():

    arquivo = "/home/karoline/Documents/IFPI/Algoritmo-e-Programa-o-IFPI/Exercicios/Sala/wordplay/words.txt"
    linhas = carregar_linhas(arquivo)
    opcao = input(menu())

    while opcao != "0":
        if opcao == "1":
            palavras_20_mais = mais_20_letras(linhas)
            listar_palavras(palavras_20_mais, "Palavras com mais de 20 letras", len(linhas))
        elif opcao == "2":
            palavras_sem_e = listar_palavras_sem_e(linhas)
            listar_palavras(palavras_sem_e, "Palavras sem 'e'", len(linhas))
        elif opcao == "3":
            proibidas = input("Letras proibidas: ")
            palavras_proibidas = avoids(linhas, proibidas)
            listar_palavras(palavras_proibidas, "Palavras sem as letras proibidas", len(linhas))

        input("Press the Enter key to continue: ")
        os.system("clear")
        opcao = input(menu())


def menu():
    texto_menu = f"""
1 - Palavras com mais de 20 caracteres
2 - Palavras sem e
3 - Sem letras proibidas
4 - Apenas letras proibidas
5 - Usa todas as letras
6 - Palavras com letra em ordem alfabética
0 - Sair

Escolha uma opção: """

    return texto_menu


def avoids(palavras, proibidas):
    for palavra in palavras:
        lista = [for letra in palavra if letra not in proibidas]

    return lista


def listar_palavras_sem_e(palavras):
    lista = [palavra for palavra in palavras if has_no_e("e", palavra)]

    return lista 


def has_no_e(letra, palavra):
    return letra not in palavra


def mais_20_letras(palavras):
    lista = [for palavra in palavras if len(palavra) > 20]

    return lista


def carregar_linhas(arquivo):
    linhas = []
    with open(arquivo, "r") as arquivo:
        for palavra in arquivo.readlines():
            linhas.append(palavra.strip())
    return linhas


def listar_palavras(palavras, titulo, total):
    print(f"""
---------------------------------
LISTA: {titulo}
---------------------------------""")
          
    for palavra in palavras:
        print(palavra)

    print("---------------------------------")

    percentual = (len(palavras) / total) * 100

    resumo = f"""
--> Palavras = {len(palavras)}
--> Total    = {total}
--> Perc (%) = {percentual:.2f}%
"""

    print(resumo)


main()