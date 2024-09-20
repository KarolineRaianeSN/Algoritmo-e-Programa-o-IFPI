from utils.menus import *
from utils.funcionalidades import *

def main():
    montadoras = [
    '123' : {
        'id': '123',
        'nome': 'Toyota',
        'pais': 'Japão',
        'ano_fundacao': 1937
    }
    ]

    opcao = input(menu_montadoras())

    match opcao:
        case "1":
            adicionar_montadora()
        case "2":
            listar_montadoras()
        case "3":
            remover_montadoras()
        case "0":
            exit()
        case _:
            print("Opcão inválida")


main()