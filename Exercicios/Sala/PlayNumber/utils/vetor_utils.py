from utils.utils import *
import random

def inicializar_vetor(vetor):
    opcao = pedir_numero("Escolha o método de inicialização:\n1. Automático\n2. Manual\n3. Carregar de arquivo\nOpção: ")

    if opcao == 1:
        tamanho = pedir_numero_positivo("Informe o tamanho do vetor: ")
        minimo = pedir_numero("Informe o valor mínimo: ")
        maximo = pedir_numero("Informe o valor máximo: ")

        vetor.extend([random.randint(minimo, maximo) for _ in range(tamanho)])

    elif opcao == 2:
        vetor.clear()
        tamanho = pedir_numero_positivo("Informe o tamanho do vetor: ")
        for i in range(tamanho):
            vetor.append(pedir_numero(f"Informe o valor para a posição {i+1}: "))

    elif opcao == 3:
        nome_arquivo = input("Informe o nome do arquivo para carregar os valores: ")
        try:
            with open(nome_arquivo, 'r') as file:
                vetor.extend([int(linha.strip()) for linha in file.readlines()])

        except FileNotFoundError:
            print("Arquivo não encontrado.")
    else:
        print("Opção inválida.")
    

def adicionar_valores(vetor, novos_valores):
    return vetor + novos_valores

def remover_por_valor(vetor, valor):
    return [v for v in vetor if v != valor]

def remover_por_posicao(vetor, posicao):
    return vetor[:posicao] + vetor[posicao+1:]

def editar_valor_por_posicao(vetor, posicao, novo_valor):
    vetor[posicao] = novo_valor
    return vetor

def salvar_em_arquivo_txt(vetor, nome_arquivo):
    with open(nome_arquivo, 'w') as file:
        for valor in vetor:
            file.write(f"{valor}\n")