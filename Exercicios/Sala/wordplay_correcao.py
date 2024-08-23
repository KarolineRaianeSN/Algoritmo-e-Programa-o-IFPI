import os

def main():
    arquivo = "words.txt"
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
            palavras_permitidas = avoids(linhas, proibidas)
            listar_palavras(palavras_permitidas, "Palavras sem as letras proibidas", len(linhas))
        elif opcao == "4":
            letras_permitidas = input("Letras permitidas: ")
            palavras_permitidas = uses_only(linhas, letras_permitidas)
            listar_palavras(palavras_permitidas, "Palavras com apenas letras permitidas", len(linhas))
        elif opcao == "5":
            letras_obrigatorias = input("Letras obrigatórias: ")
            palavras_com_todas = uses_all(linhas, letras_obrigatorias)
            listar_palavras(palavras_com_todas, "Palavras com todas as letras obrigatórias", len(linhas))
        elif opcao == "6":
            palavras_abc = is_abecedarian(linhas)
            listar_palavras(palavras_abc, "Palavras em ordem alfabética", len(linhas))

        input("Pressione Enter para continuar: ")
        os.system("clear")
        opcao = input(menu())

def menu():
    texto_menu = """
1 - Palavras com mais de 20 caracteres
2 - Palavras sem 'e'
3 - Sem letras proibidas
4 - Apenas letras permitidas
5 - Usa todas as letras obrigatórias
6 - Palavras em ordem alfabética
0 - Sair

Escolha uma opção: """
    return texto_menu

def carregar_linhas(arquivo):
    linhas = []
    with open(arquivo, "r") as f:
        for linha in f:
            linhas.append(linha.strip())
    return linhas

def mais_20_letras(palavras):
    return [palavra for palavra in palavras if len(palavra) > 20]

def has_no_e(palavra):
    return 'e' not in palavra

def listar_palavras_sem_e(palavras):
    return [palavra for palavra in palavras if has_no_e(palavra)]

def avoids(palavras, proibidas):
    return [palavra for palavra in palavras if all(letra not in palavra for letra in proibidas)]

def uses_only(palavras, permitidas):
    return [palavra for palavra in palavras if all(letra in permitidas for letra in palavra)]

def uses_all(palavras, obrigatorias):
    return [palavra for palavra in palavras if all(letra in palavra for letra in obrigatorias)]

def is_abecedarian(palavras):
    return [palavra for palavra in palavras if list(palavra) == sorted(palavra)]

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

if __name__ == "__main__":
    main()
