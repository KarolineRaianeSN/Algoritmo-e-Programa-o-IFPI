from veiculos import veiculos_v3
from modelos import modelos_v2
from montadoras import montadoras_v1
from utils.funcionalidades import *
from utils.funcionalidades_modelos import *
from utils.funcionalidades_montadoras import *
from utils.funcionalidades_veiculos import *
from utils.menus import *
from utils.ulid import gerar_ulid

def main():
    opcao = input(menu_principal())

    while opcao != '0':
        match opcao:
            case '1':
                limpar_tela()
                montadoras_v1()
            case '2':
                limpar_tela()
                modelos_v2()
            case '3':
                limpar_tela()
                veiculos_v3()
            case _:
                print("Opção inválida. Tente novamente.")

        # Após cada operação, pausar e limpar a tela
        input("Pressione Enter para continuar...")
        limpar_tela()

        # Exibir o menu novamente após uma operação
        opcao = input(menu_principal())

    print("Saindo do programa.")

if __name__ == "__main__":
    main()