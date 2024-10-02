from utils.funcionalidades_modelos import *
from utils.menus import *
from utils.funcionalidades import *
from montadoras import lista_montadoras
import pprint

global modelos

lista_modelos = [
    {
        'nome': 'Corolla',
        'montadora': 'Toyota',
        'valor_referencia': 120000.0,
        'motoracao': '1.8L',
        'turbo': False,
        'automatico': True
    },
    {
        'nome': 'Civic',
        'montadora': 'Honda',
        'valor_referencia': 110000.0,
        'motoracao': '2.0L',
        'turbo': True,
        'automatico': False
    },
    {
        'nome': 'Golf',
        'montadora': 'Volkswagen',
        'valor_referencia': 100000.0,
        'motoracao': '1.6L',
        'turbo': False,
        'automatico': True
    }
]
def modelos_v2():

    opcao = input(menu_modelos())

    while opcao != "0":
        limpar_tela()

        match opcao:
            case "1":
                adicionar_modelo(lista_modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "2":
                listar_modelos(lista_modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "3":
                encontrar_modelos(lista_modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "4":
                atualizar_modelos(lista_modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "5":
                remover_modelo(lista_modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "6":
                carregar_modelos()
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case "7":
                gravar_modelos(lista_modelos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())
            case _:
                print("Opcão inválida")
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_modelos())

if __name__ == "__main__":
    modelos_v2()