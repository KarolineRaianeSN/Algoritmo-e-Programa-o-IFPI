from utils.utils import *
from utils.vetor_utils import *
from utils.vetor_funcionalidades import *

def executar_menu_atualizar_valores(vetor):
    while True:
        limpar_tela()
        print("""
1. Multiplicar por um valor
2. Elevar a um valor (exponenciação)
3. Reduzir a uma fração
4. Substituir valores negativos por um número aleatório
5. Ordenar valores
6. Embaralhar valores
0. Voltar ao menu principal
""")
        opcao_submenu = pedir_numero("Escolha uma opção: ")

        if opcao_submenu < 0 or opcao_submenu > 6:  # Verificar se a opção é inválida
            print("Opção inválida no submenu de atualização!")
            input("\nPressione Enter para continuar...")
        else:
            if opcao_submenu == 0:
                return  # Voltar ao menu principal
            elif opcao_submenu == 1:
                multiplicar_por_valor(vetor)
            elif opcao_submenu == 2:
                elevar_a_valor(vetor)
            elif opcao_submenu == 3:
                reduzir_a_fracao(vetor)
            elif opcao_submenu == 4:
                substituir_negativos_por_aleatorio(vetor)
            elif opcao_submenu == 5:
                ordenar_valores(vetor)
            elif opcao_submenu == 6:
                embaralhar_valores(vetor)

            input("\nPressione Enter para continuar...")

def multiplicar_por_valor(vetor):
    multiplicador = pedir_numero_positivo("Informe o multiplicador: ")
    vetor[:] = [x * multiplicador for x in vetor]

def elevar_a_valor(vetor):
    expoente = pedir_numero_positivo("Informe o expoente: ")
    vetor[:] = [x ** expoente for x in vetor]

def reduzir_a_fracao(vetor):
    fracao = pedir_numero_positivo("Informe a fração (ex: 0.2 para 1/5): ")
    vetor[:] = [x * fracao for x in vetor]

def substituir_negativos_por_aleatorio(vetor):
    minimo = pedir_numero_positivo("Informe o valor mínimo: ")
    maximo = pedir_numero_positivo("Informe o valor máximo: ")
    vetor[:] = [x if x >= 0 else random.uniform(minimo, maximo) for x in vetor]

def ordenar_valores(vetor):
    decrescente = bool(int(pedir_numero_positivo("Ordenar em ordem decrescente? (1: Sim, 0: Não): ")))
    vetor[:] = sorted(vetor, reverse=decrescente)

def embaralhar_valores(vetor):
    random.shuffle(vetor)