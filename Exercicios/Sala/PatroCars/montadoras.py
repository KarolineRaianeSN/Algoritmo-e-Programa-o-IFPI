from utils.menus import *
from utils.funcionalidades import *
from utils.funcionalidades_montadoras import *

global montadoras

lista_montadoras = [
    {
        'nome': 'Toyota',
        'pais': 'Japão',
        'ano_fundacao': 1937
    },
    {
        'nome': 'Honda',
        'pais': 'Japão',
        'ano_fundacao': 1948
    },
    {
        'nome': 'Volkswagen',
        'pais': 'Alemanha',
        'ano_fundacao': 1937
    }
]
def montadoras_v1():

    opcao = input(menu_montadoras())

    while opcao != "0":
        limpar_tela()

        match opcao:
            case "1":
                adicionar_montadora(lista_montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "2":
                listar_montadoras(lista_montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "3":
                encontrar_montadora(lista_montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "4":
                atualizar_montadora(lista_montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "5":
                remover_montadora(lista_montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "6":
                carregar_montadoras()
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case "7":
                gravar_montadoras(lista_montadoras)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
            case _:
                print("Opcão inválida")
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_montadoras())
    

if __name__ == "__main__":
    montadoras_v1()