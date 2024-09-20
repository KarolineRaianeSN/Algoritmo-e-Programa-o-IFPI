from utils.ulid import gerar_ulid
from utils.funcionalidades import limpar_tela 
import pprint


def adicionar_montadora(montadoras: list):
    """Cria e adiciona montadora na lista"""
    limpar_tela()

    nome = input("Nome da montadora: ")
    pais = input("País: ")
    ano_fundacao = int(input("Ano de fundação: "))

    montadoras.append({
        'id': gerar_ulid(),
        'nome': nome,
        'pais': pais,
        'ano_fundacao': ano_fundacao
    })

    
def listar_montadoras(montadoras: list):
    """Imprime as montadoras na tela"""
    limpar_tela()
    
    for montadora in montadoras:
        pprint.pprint(montadora)


def remover_montadora():
    pass


def atualizar_montadora():
    pass


def encontrar_montadora():
    pass