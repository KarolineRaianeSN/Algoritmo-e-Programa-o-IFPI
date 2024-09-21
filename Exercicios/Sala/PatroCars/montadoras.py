from utils.menus import *
from utils.funcionalidades import *
from utils.funcionalidades_montadoras import *

def main():
    montadoras = [
        {
        'id': '123',
        'nome': 'Toyota',
        'pais': 'Japão',
        'ano_fundacao': 1937
    }
    ]

    opcao = input(menu_montadoras())

    while opcao != "0":
        limpar_tela()

        match opcao:
            case "1":
                adicionar_montadora(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "2":
                listar_montadoras(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "3":
                encontrar_montadora(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "4":
                atualizar_montadora(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "5":
                remover_montadora(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "6":
                carregar_montadoras(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "7":
                gravar_montadoras(montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case _:
                print("Opcão inválida")
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
    

main()