from utils.ulid import gerar_ulid
from utils.funcionalidades import *
from utils.menus import *
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
    
    montadoras_ordenadas = ordenar_montadoras(montadoras)

    for montadora in montadoras_ordenadas:
        pprint.pprint(montadora)

    print(f"Status: {len(montadoras)} montadoras cadastradas")


def remover_montadora(montadoras):
    """Lista montadoras e depois remove com base no ID"""
    listar_montadoras(montadoras)
    ID = input("ID da montadora: ")

    vetor_novo = [montadora for montadora in montadoras if montadora['id'] != ID]
    montadoras.clear()
    montadoras.extend(vetor_novo)


def atualizar_montadora(montadoras):
    """Lista montadoras e depois atualiza com base na opção escolhida"""

    listar_montadoras(montadoras)
    opcao = input(menu_atualizar_montadora())

    match opcao:
        case "1":
            nome = input("Nome atual da montadora: ")
            novo_nome = input("Novo nome da montadora: ")
            for montadora in montadoras:
                if montadora['nome'] == nome:
                    montadora['nome'] = novo_nome

        case "2":
            pais = input("País: ")
            novo_pais = input("Novo país: ")
            for montadora in montadoras:
                if montadora['pais'] == pais:
                    montadora['pais'] = novo_pais

        case "3":
            ano_fundacao = int(input("Atual ano de fundação: "))
            novo_ano_fundacao = int(input("Novo ano de fundação: "))
            for montadora in montadoras:
                if montadora['ano_fundacao'] == ano_fundacao:
                    montadora['ano_fundacao'] = novo_ano_fundacao

        case "4":
            nome = input("Nome atual da montadora: ")
            novo_nome = input("Novo nome da montadora: ")
            pais = input("País atual da montadora: ")
            novo_pais = input("Novo país da montadora: ")
            ano_fundacao = int(input("Atual ano de fundação: "))
            novo_ano_fundacao = int(input("Novo ano de fundação: "))
            for montadora in montadoras:
                if montadora['nome'] == nome:
                    montadora['nome'] = novo_nome
                if montadora['pais'] == pais:
                    montadora['pais'] == novo_pais
                if montadora['ano_fundacao'] == ano_fundacao:
                    montadora['ano_fundacao'] = novo_ano_fundacao

        case "0":
            opcao = input(menu_montadoras())

        case _:
            print("Opcão inválida")
            opcao = input(menu_montadoras())


def encontrar_montadora(montadoras: list):
    """Encontra montadora e imprime na tela"""

    opcao = input(filtros_montadoras())

    match opcao:
        case "1":
            nome = input("Nome da montadora: ")
            filtro = lambda montadora: nome in montadora["nome"]
        case "2":
            pais = input("País: ")
            filtro = lambda montadora: pais in montadora["pais"]
        case "3":
            ano_fundacao = int(input("Ano de fundação: "))
            filtro = lambda montadora: ano_fundacao == montadora["ano_fundacao"]
        case "0":
            opcao = input(menu_montadoras())
        case _:
            print("Opcão inválida")
            opcao = input(menu_montadoras())

    
    montadoras_filtradas = list(filter(filtro, montadoras))

    return listar_montadoras(montadoras_filtradas)


def ordenar_montadoras(montadoras):
    """Ordena montadoras de acordo com critério escolhido"""

    if not montadoras:
        print("Nenhuma montadora cadastrada.")
        return montadoras

    ordenar_por = input("Ordenar por (nome/pais/ano_fundacao): ").lower()
    direcao = input("Ordem (ASC/DESC): ").upper()

    if ordenar_por not in ["nome", "pais", "ano_fundacao"]:
        print("Opcão inválida")
        return ordenar_montadoras(montadoras)

    if direcao not in ["ASC", "DESC"]:
        print("Opcão inválida")
        return ordenar_montadoras(montadoras)

    return ordenar_lista(montadoras, ordenar_por, direcao)


def carregar_montadoras():
    arquivo = input("Nome do arquivo(ex: montadoras.txt): ")

    with open(arquivo, 'r') as arquivo:
        chaves = ["nome", "pais", "ano_fundacao"]

        dados = []

        for linha in arquivo:
            dados.append(dict(zip(chaves, linha.strip().split(';'))))
    
    return dados


def gravar_montadoras(montadoras):
    nome_arquivo = input("Nome do arquivo(ex: montadoras.txt): ")

    with open(nome_arquivo, 'w') as arquivo:
        for montadora in montadoras:
            arquivo.write(f"{montadora['nome']};{montadora['pais']};{montadora['ano_fundacao']}\n")

    print("Dados gravados com sucesso!")