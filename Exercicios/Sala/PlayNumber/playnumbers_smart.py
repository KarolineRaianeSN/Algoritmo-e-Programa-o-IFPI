from utils.utils import *
from utils.vetor_utils import *
from utils.vetor_funcionalidades import *
from utils.menu_atualizar_valores_smart import *
from functools import reduce

def menu():

    vetor = []

    mostrar_menu()
    opcao = pedir_numero("Escolha uma opção: ")
    
    while opcao != 0:
        limpar_tela()
        opcoes = {
            1: lambda: inicializar_vetor(vetor),
            2: lambda: mostrar_valores(vetor),
            3: lambda: resetar_vetor(vetor, pedir_numero("Informe o valor padrão: ")),
            4: lambda: print(f"Quantidade de itens no vetor: {quantidade_itens(vetor)}"),
            5: lambda: print(f"Menor valor: {min(vetor)}, Maior valor: {max(vetor)}"),
            6: lambda: print(f"Somatorio dos valores: {reduce(lambda x, y: x + y, vetor)}"),
            7: lambda: print(f"M dia dos valores: {reduce(lambda x, y: x + y, vetor) / len(vetor)}"),
            8: lambda: print(f"Valores positivos: {list(filter(lambda x: x > 0, vetor))}, Quantidade: {len(list(filter(lambda x: x > 0, vetor)))}"),
            9: lambda: print(f"Valores negativos: {list(filter(lambda x: x < 0, vetor))}, Quantidade: {len(list(filter(lambda x: x < 0, vetor)))}"),
            10: lambda: executar_menu_atualizar_valores(vetor),
            11: lambda: adicionar_valores(vetor),
            12: lambda: remover_por_valor(vetor),
            13: lambda: remover_por_posicao(vetor),
            14: lambda: editar_valor_por_posicao(vetor, int(pedir_numero_positivo("Informe a posi o a ser editada: ")) - 1, pedir_numero("Informe o novo valor: ")),
            15: lambda: salvar_em_arquivo_txt(vetor, input("Informe o nome do arquivo para salvar (ex: valores.txt): ")),
            16: lambda: (salvar_em_arquivo_txt(vetor, 'valores_salvos.txt'), print("Vetor salvo e programa encerrado."))
        }

        if opcao in opcoes:
            opcoes[opcao]()
        else:
            print("Opção inválida!")

        
        input("\nPressione Enter para continuar...")
        limpar_tela()
        mostrar_menu()
        opcao = pedir_numero("Escolha uma opção: ")

if __name__ == "__main__":
    menu()
