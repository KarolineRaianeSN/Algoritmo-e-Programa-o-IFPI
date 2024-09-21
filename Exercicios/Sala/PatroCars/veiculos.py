from modelos import modelos
from montadoras import montadoras
import pprint
from utils.funcionalidades import *
from utils.funcionalidades_veiculos import *
from utils.menus import *
from utils.ulid import gerar_ulid


def veiculos():
    veiculos = []

    opcao = input(menu_veiculos())

    while opcao != "0":
        limpar_tela()

        match opcao:
            case "1":
                adicionar_veiculo(veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "2":
                contar_veiculos(veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "3":
                encontrar_veiculo(veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "4":
                atualizar_veiculo(veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "5":
                remover_veiculo(veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "6":
                carregar_veiculos()
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case "7":
                gravar_veiculos(veiculos)
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())
            case _:
                print("Opcão inválida")
                input("Press Enter to continue...")
                limpar_tela()
                opcao = input(menu_veiculos())


if __name__ == "__main__":
    veiculos()
