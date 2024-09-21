from utils import *
from montadoras import montadoras
from modelos import modelos
import pprint

def adicionar_veiculo(veiculos: list):
    """Lista montadoras e modelos e pede ao usuários para escolher montadora e modelo, pede os dados e adiciona na lista"""

    limpar_tela()

    if not montadoras:
        print("Nenhuma montadora cadastrada. Cadastre uma montadora primeiro.")
        return
    
    if not modelos:
        print("Nenhum modelo cadastrado. Cadastre um modelo primeiro.")
        return
    
    print("=================== MONTADORAS CADASTRADAS ===================")
    for i, montadora in enumerate(montadoras):
        print(f"{i + 1}. {montadora['nome']}")
    
    escolha = int(input("Digite o número da montadora: ")) - 1
    montadora_selecionada = montadoras[escolha]

    print("=================== MODELOS CADASTRADOS ===================")
    for i, modelo in enumerate(modelos):
        print(f"{i + 1}. {modelo['nome']}")

    escolha = int(input("Digite o número do modelo: ")) - 1
    modelo_selecionado = modelos[escolha]

    nome = input("Nome do veículo: ")
    ano = int(input("Ano: "))

    # (id: ULID, modelo_id: string, cor: string, ano_fabricacao: number, ano_modelo: number, valor: number, placa: string, vendido: boolean)

    nome = input("Nome do veículo: ")
    ano_fabricacao = int(input("Ano de fabricação: "))
    ano_modelo = int(input("Ano do modelo: "))
    placa = input("Placa: ")
    vendido = bool(input("Vendido (1: sim | 2: nao): "))
    
    veiculos.append({
        'id': gerar_ulid(),
        'montadora': montadora_selecionada,
        'modelo': modelo_selecionado,
        'nome': nome,
        'ano_fabricacao': ano_fabricacao,
        'ano_modelo': ano_modelo,
        'valor': modelo_selecionado,['valor_referencia']: valor,
        'placa': placa,
        'vendido': False
    })

    print("Veículo adicionado com sucesso!")


def listar_veiculos(veiculos):
    """Ordena e imprime veiculos na tela"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    ordenar_veiculos(veiculos)

    for veiculo in veiculos:
        pprint.pprint(veiculo)

    print(f"Status: {len(veiculos)} veículos")


def ordenar_veiculos(veiculos):
    """Ordena veiculos de acordo com critério escolhido"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    ordenar_por = input("Ordenar por (nome/montadora/valor_referencia/motoracao/turbo/automatico): ").lower()
    direcao = input("Ordem (ASC/DESC): ").upper()

    if ordenar_por not in ["nome", "montadora", "valor_referencia", "motoracao", "turbo", "automatico"]:
        print("Opcão inválida")
        return ordenar_veiculos(veiculos)

    if direcao not in ["ASC", "DESC"]:
        print("Opcão inválida")
        return ordenar_veiculos(veiculos)

    return ordenar_lista(veiculos, ordenar_por, direcao)


def encontrar_veiculos(veiculos):
    """Encontra veículo e imprime na tela"""

    opcao = input(filtros_veiculos())

    match opcao:
        case "1":
            nome = input("Nome do veículo: ")
            filtro = lambda veiculo: nome in veiculo["nome"]
        case "2":
            montadora_id = input("ID da montadora: ")
            filtro = lambda veiculo: montadora_id in veiculo["montadora"]
        case "3":
            modelo_id = input("ID do modelo: ")
            filtro = lambda veiculo: modelo_id in veiculo["modelo"]
        case "4":
            ano_fabricacao = input("Ano de fabricação: ")
            filtro = lambda veiculo: ano_fabricacao in veiculo["ano_fabricacao"]
        case "5":
            ano_modelo = input("Ano de modelo: ")
            filtro = lambda veiculo: ano_modelo in veiculo["ano_modelo"]
        case "6":
            placa = input("Placa: ")
            filtro = lambda veiculo: placa in veiculo["placa"]
        case "7":
            vendido = input("Vendido (1: sim | 2: nao): ")
            filtro = lambda veiculo: vendido in veiculo["vendido"]
        case _:
            print("Opcão inválida")
            return encontrar_veiculos(veiculos)
        
    veiculos_encontrados = list(filter(filtro, veiculos))

    return listar_veiculos(veiculos_encontrados)


def atualizar_veiculos(veiculos):
    """Atualiza veículo na lista de acordo com critério escolhido"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    veiculos_encontrados = encontrar_veiculos(veiculos)

    if not veiculos_encontrados:
        print("Nenhum veículo encontrado.")
        return veiculos

    opcao = input(menu_atualizar_veiculos(veiculos_encontrados))

    match opcao:
        case "1":
            nome = input("Nome atual do veículo: ")
            novo_nome = input("Novo nome do veículo: ")
            for veiculo in veiculos_encontrados:
                if veiculo["nome"] == nome:
                    veiculo["nome"] = novo_nome

        case "2":
            modelo = input("Modelo atual do veículo: ")
            novo_modelo = input("Novo modelo do veículo: ")
            for veiculo in veiculos_encontrados:
                if veiculo["modelo"] == modelo:
                    veiculo["modelo"] = novo_modelo

        case "3":
            cor = input("Cor atual do veículo: ")
            nova_cor = input("Nova cor do veículo: ")
            for veiculo in veiculos_encontrados:
                if veiculo["cor"] == cor:
                    veiculo["cor"] = nova_cor

        case "4":
            ano_fabricacao = input("Ano de fabricação atual do veículo: ")
            novo_ano_fabricacao = input("Novo ano de fabricação do veículo: ")
            for veiculo in veiculos_encontrados:
                if veiculo["ano_fabricacao"] == ano_fabricacao:
                    veiculo["ano_fabricacao"] = novo_ano_fabricacao

        case "5":
            ano_modelo = input("Ano de modelo atual do veículo: ")
            novo_ano_modelo = input("Novo ano de modelo do veículo: ")
            for veiculo in veiculos_encontrados:
                if veiculo["ano_modelo"] == ano_modelo:
                    veiculo["ano_modelo"] = novo_ano_modelo

        case "6":
            placa = input("Placa atual do veículo: ")
            nova_placa = input("Nova placa do veículo: ")
            for veiculo in veiculos_encontrados:
                if veiculo["placa"] == placa:
                    veiculo["placa"] = nova_placa

        case "7":
            vendido = input("Vendido atual do veículo (1: sim | 2: nao): ")
            novo_vendido = input("Novo vendido do veículo (1: sim | 2: nao): ")
            for veiculo in veiculos_encontrados:
                if veiculo["vendido"] == vendido:
                    veiculo["vendido"] = novo_vendido

        case "0":
            opcao = input(menu_veiculos())

        case _:
            print("Opcão inválida")
            return atualizar_veiculos(veiculos)


def remover_veiculos(veiculos):
    """Remove veículo de acordo com id do veículo"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    listar_veiculos(veiculos)

    id_veiculo = input("ID do veículo: ")
    vetor_novo = [veiculo for veiculo in veiculos if veiculo["id"] != id_veiculo]
    
    veiculos.clear()
    veiculos.extend(vetor_novo)


def carregar_veiculos():
    """Carrega veículos de um arquivo"""

    arquivo = input("Nome do arquivo: ")

    with open(arquivo, "r") as arquivo:
        chaves = ["id", "nome", "modelo", "cor", "ano_fabricacao", "ano_modelo", "placa", "vendido"]

        dados = []

        for linha in arquivo:
            dados.append({chave: valor for chave, valor in zip(chaves, linha.strip().split(";"))})

        return dados


def gravar_veiculos():
    """Grava veículos em um arquivo"""

    arquivo = input("Nome do arquivo: ")

    with open(arquivo, "w") as arquivo:
        for veiculo in veiculos:
            arquivo.write(f"{veiculo['id']};{veiculo['nome']};{veiculo['modelo']};{veiculo['cor']};{veiculo['ano_fabricacao']};{veiculo['ano_modelo']};{veiculo['placa']};{veiculo['vendido']}\n")

    print("Dados gravados com sucesso!")