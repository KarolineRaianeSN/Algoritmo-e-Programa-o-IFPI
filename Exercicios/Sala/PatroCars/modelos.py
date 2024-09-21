from utils.funcionalidades_modelos import *
from utils.menus import *
from utils.funcionalidades import *
from montadoras import montadoras
import pprint

def modelos():
    modelos = [
    [
    {
        'id': 'D8K7L9W0P2Q3S4F6A1G2B5C3E4',
        'montadora': '123',
        'nome': 'Corolla',
        'valor_referencia': 120000.0,
        'motorizacao': 1.8,
        'turbo': False,
        'automatico': True
    }
]
]

    opcao = input(menu_modelos())

    while opcao != "0":
        limpar_tela()

        match opcao:
            case "1":
                adicionar_modelo(modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "2":
                listar_modelos(modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "3":
                encontrar_modelos(modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "4":
                atualizar_modelos(modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "5":
                remover_modelo(modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "6":
                carregar_modelos()
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "7":
                gravar_modelos(modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case _:
                print("Opcão inválida")
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())

if __name__ == "__main__":
    modelos()