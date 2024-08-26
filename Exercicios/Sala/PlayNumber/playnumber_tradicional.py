from utils.utils import *
from utils.vetor_utils import *
from utils.vetor_funcionalidades import *

def menu():
    vetor = []

    mostrar_menu()
    opcao = pedir_numero("Escolha uma opção: ")
    
    while opcao != 0:
        limpar_tela()
        
        if opcao == 1:
            inicializar_vetor(vetor)
        elif opcao == 2:
            mostrar_valores(vetor)
        elif opcao == 3:
            vetor = resetar_vetor(vetor, pedir_numero("Informe o valor padrão: "))
        elif opcao == 4:
            print(f"Quantidade de itens no vetor: {quantidade_itens(vetor)}")
        elif opcao == 5:
            menor, maior = menor_maior_valores(vetor)
            print(f"Menor valor: {menor}, Maior valor: {maior}")
        elif opcao == 6:
            print(f"Somatório dos valores: {somatorio_valores(vetor)}")
        elif opcao == 7:
            print(f"Média dos valores: {media_valores(vetor)}")
        elif opcao == 8:
            positivos, qtd = valores_positivos(vetor)
            print(f"Valores positivos: {positivos}, Quantidade: {qtd}")
        elif opcao == 9:
            negativos, qtd = valores_negativos(vetor)
            print(f"Valores negativos: {negativos}, Quantidade: {qtd}")
        elif opcao == 10:
            sub_opcao = menu_atualizar_valores()
            if sub_opcao == 1:
                vetor = multiplicar_valores(vetor, pedir_numero("Informe o multiplicador: "))
            elif sub_opcao == 2:
                vetor = elevar_valores(vetor, pedir_numero("Informe o expoente: "))
            elif sub_opcao == 3:
                vetor = reduzir_por_fracao(vetor, pedir_numero("Informe a fração (ex: 0.2 para 1/5): "))
            elif sub_opcao == 4:
                min_val = pedir_numero("Informe o valor mínimo: ")
                max_val = pedir_numero("Informe o valor máximo: ")
                vetor = substituir_negativos(vetor, min_val, max_val)
            elif sub_opcao == 5:
                reverse = bool(int(pedir_numero("Ordenar em ordem decrescente? (1: Sim, 0: Não): ")))
                vetor = ordenar_valores(vetor, reverse)
            elif sub_opcao == 6:
                vetor = embaralhar_valores(vetor)
        elif opcao == 11:
            novos_valores = [pedir_numero("Informe o valor: ") for _ in range(int(pedir_numero("Quantos valores deseja adicionar? ")))]
            vetor = adicionar_valores(vetor, novos_valores)
        elif opcao == 12:
            vetor = remover_por_valor(vetor, pedir_numero("Informe o valor a ser removido: "))
        elif opcao == 13:
            vetor = remover_por_posicao(vetor, int(pedir_numero("Informe a posição a ser removida: ")) - 1)
        elif opcao == 14:
            posicao = int(pedir_numero("Informe a posição a ser editada: ")) - 1
            novo_valor = pedir_numero("Informe o novo valor: ")
            vetor = editar_valor_por_posicao(vetor, posicao, novo_valor)
        elif opcao == 15:
            nome_arquivo = input("Informe o nome do arquivo para salvar (ex: valores.txt): ")
            salvar_em_arquivo_txt(vetor, nome_arquivo)
        elif opcao == 16:
            salvar_em_arquivo_txt(vetor, 'valores_salvos.txt')
            print("Vetor salvo e programa encerrado.")
            break
        
        input("Pressione Enter para continuar")
        limpar_tela()
        mostrar_menu()
        opcao = pedir_numero("Escolha uma opção: ")


if __name__ == "__main__":
    menu()
