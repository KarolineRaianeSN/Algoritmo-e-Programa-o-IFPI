from modelos import modelos_v2
from montadoras import montadoras_v1
import pprint
from utils.funcionalidades import *
from utils.funcionalidades_veiculos import *
from utils.menus import *
from utils.ulid import gerar_ulid


lista_veiculos = [
    {
        'id': 'G5H7J9K0L2M4N6O8P1Q3R5S7V9',
        'montadora' : 'Toyota',
        'nome': 'Corolla XRS',
        'modelo': 'Corolla',
        'cor': 'Prata',
        'ano_fabricacao': 2020,
        'ano_modelo': 2021,
        'placa': 'ABC-1234',
        'valor': '500000',
        'vendido': False
    },
    {
        'id': 'G5H7J9K0L2M4N6O8P1Q3R5S7V8',
        'montadora' : 'Honda',
        'nome': 'Civic EX',
        'modelo': 'Civic',
        'cor': 'Preto',
        'ano_fabricacao': 2019,
        'ano_modelo': 2020,
        'valor': '400000',
        'placa': 'DEF-5678',
        'vendido': False
    },
    {
        'id': 'G5H7J9K0L2M4N6O8P1Q3R5S7V7',
        'montadora' : 'Volkswagen',
        'nome': 'Golf GTI',
        'modelo': 'Golf',
        'cor': 'Branco',
        'ano_fabricacao': 2018,
        'ano_modelo': 2019,
        'valor': '300000',
        'placa': 'GHI-9012',
        'vendido': False
    }
]


def veiculos_v3():
    global lista_veiculos

    opcao = input(menu_veiculos())

    while opcao != "0":
        limpar_tela()

        match opcao:
            case "1":
                adicionar_veiculo(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "2":
                listar_veiculos(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "3":
                encontrar_veiculos(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "4":
                lista_veiculos = atualizar_veiculos(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "5":
                lista_veiculos = remover_veiculos(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "6":
                carregar_veiculos(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "7":
                gravar_veiculos(lista_veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case _:
                print("Opcão inválida")
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())


if __name__ == "__main__":
    veiculos_v3()
