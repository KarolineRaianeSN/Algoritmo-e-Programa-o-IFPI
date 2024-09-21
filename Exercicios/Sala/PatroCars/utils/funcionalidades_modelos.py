from utils.ulid import gerar_ulid
from utils.funcionalidades import *
from utils.menus import *
from utils.funcionalidades_montadoras import *
from montadoras import montadoras
import pprint


def adicionar_modelo(modelos: list):
    """Lista montadoras, pede ao usuário para escolher, pede os dados e adiciona na lista"""
    limpar_tela()

    if not montadoras:
        print("Nenhuma montadora cadastrada. Cadastre uma montadora primeiro.")
        return
    
    print("=================== MONTADORAS CADASTRADAS ===================")
    for i, montadora in enumerate(montadoras):
        print(f"{i + 1}. {montadora['nome']}")
    
    escolha = int(input("Digite o número da montadora: ")) - 1
    montadora_selecionada = montadoras[escolha]

    nome = input("Nome do modelo: ")
    valor_referencia = float(input("Valor de referência: "))
    motorizacao = float(input("Motorização: "))
    turbo = bool(input("Turbo(1: sim | 2: nao): "))
    automatico = bool(input("Automoção(1: sim | 2: nao): "))

    modelos.append({
        'id': gerar_ulid(),
        'montadora': montadora_selecionada,
        'nome': nome,
        'valor_referencia': valor_referencia,
        'motorizacao': motorizacao,
        'turbo': turbo,
        'automatico': automatico
    })


def listar_modelos(veiculos):
    """Imprime veiculos na tela"""
    limpar_tela()

    ordenar_modelos(veiculos)

    for veiculo in veiculos:
        pprint.pprint(veiculo)

    print(f"Status: {len(veiculos)} modelos cadastrados")


def ordenar_modelos(modelos):
    """Ordena modelos de acordo com critério escolhido"""

    if not modelos:
        print("Nenhum veículo cadastrado.")
        return modelos

    ordenar_por = input("Ordenar por (nome/montadora/valor_referencia/motoracao/turbo/automatico): ").lower()
    direcao = input("Ordem (ASC/DESC): ").upper()

    if ordenar_por not in ["nome", "montadora", "valor_referencia", "motoracao", "turbo", "automatico"]:
        print("Opcão inválida")
        return ordenar_modelos(modelos)

    if direcao not in ["ASC", "DESC"]:
        print("Opcão inválida")
        return ordenar_modelos(modelos)

    return ordenar_lista(modelos, ordenar_por, direcao)


def encontrar_modelos(veiculos):
    """Encontra veículo e imprime na tela"""

    opcao = input(filtros_modelos())

    match opcao:
        case "1":
            nome = input("Nome do veículo: ")
            filtro = lambda veiculo: nome in veiculo["nome"]
        case "2":
            montadora_id = input("ID da montadora: ")
            filtro = lambda veiculo: montadora_id in veiculo["montadora"]
        case "3":
            valor_referencia = float(input("Valor de referência: "))
            filtro = lambda veiculo: valor_referencia == veiculo["valor_referencia"]
        case "4":
            motoracao = int(input("Motoração: "))
            filtro = lambda veiculo: motoracao == veiculo["motoracao"]
        case "5":
            turbo = bool(input("Turbo(1: sim | 2: nao): "))
            filtro = lambda veiculo: turbo == veiculo["turbo"]
        case "6":
            automatico = bool(input("Automoção(1: sim | 2: nao): "))
            filtro = lambda veiculo: automatico == veiculo["automatico"]
        case "0":
            opcao = input(menu_modelos())
        case _:
            print("Opcão inválida")
            opcao = input(menu_modelos())

    veiculos_filrados = list(filter(filtro, veiculos))

    return listar_modelos(veiculos_filrados)


def atualizar_modelos(veiculos):
    """Atualiza veículo na lista"""

    listar_modelos(veiculos)
    opcao = input(menu_atualizar_modelos(veiculos))


    match opcao:
        case "1":
            nome = input("Nome atual do veículo: ")
            novo_nome = input("Novo nome do veículo: ")
            for veiculo in veiculos:
                if veiculo['nome'] == nome:
                    veiculo['nome'] = novo_nome

        case "2":
            montadora_id = input("ID da montadora: ")
            novo_montadora_id = input("Novo ID da montadora: ")
            for veiculo in veiculos:
                if veiculo['montadora'] == montadora_id:
                    veiculo['montadora'] = novo_montadora_id

        case "3":
            valor_referencia = float(input("Atual valor de referência: "))
            novo_valor_referencia = float(input("Novo valor de referência: "))
            for veiculo in veiculos:
                if veiculo['valor_referencia'] == valor_referencia:
                    veiculo['valor_referencia'] = novo_valor_referencia

        case "4":
            motoracao = int(input("Atual motoração: "))
            novo_motoracao = int(input("Novo motoração: "))
            for veiculo in veiculos:
                if veiculo['motoracao'] == motoracao:
                    veiculo['motoracao'] = novo_motoracao

        case "5":
            turbo = bool(input("Atual turbo: "))
            novo_turbo = bool(input("Novo turbo: "))
            for veiculo in veiculos:
                if veiculo['turbo'] == turbo:
                    veiculo['turbo'] = novo_turbo

        case "6":
            automatico = bool(input("Atual automóvel: "))
            novo_automatico = bool(input("Novo automóvel: "))
            for veiculo in veiculos:
                if veiculo['automatico'] == automatico:
                    veiculo['automatico'] = novo_automatico
        
        case "7":
            nome = input("Nome atual do veículo: ")
            novo_nome = input("Novo nome do veículo: ")
            montadora_id = input("ID da montadora: ")
            novo_montadora_id = input("Novo ID da montadora: ")
            valor_referencia = float(input("Atual valor de referência: "))
            novo_valor_referencia = float(input("Novo valor de referência: "))
            motoracao = int(input("Atual motoração: "))
            novo_motoracao = int(input("Novo motoração: "))
            turbo = bool(input("Atual turbo: "))
            novo_turbo = bool(input("Novo turbo: "))
            automatico = bool(input("Atual automóvel: "))
            novo_automatico = bool(input("Novo automóvel: "))

            for veiculo in veiculos:
                if veiculo['nome'] == nome:
                    veiculo['nome'] = novo_nome
                if veiculo['montadora'] == montadora_id:
                    veiculo['montadora'] = novo_montadora_id
                if veiculo['valor_referencia'] == valor_referencia:
                    veiculo['valor_referencia'] = novo_valor_referencia
                if veiculo['motoracao'] == motoracao:
                    veiculo['motoracao'] = novo_motoracao
                if veiculo['turbo'] == turbo:
                    veiculo['turbo'] = novo_turbo
                if veiculo['automatico'] == automatico:
                    veiculo['automatico'] = novo_automatico


        case "0":
            opcao = input(menu_modelos())
        case _:
            print("Opcão inválida")
            opcao = input(menu_modelos())

def carregar_modelos():
    """Carrega veículos do arquivo"""
    arquivo = input("Nome do arquivo: ")

    with open(arquivo, "r") as arquivo:
        chaves = ["nome", "montadora", "valor_referencia", "motoracao", "turbo", "automatico"]

        dados = []

        for linha in arquivo:
            dados.append({chave: valor for chave, valor in zip(chaves, linha.strip().split(","))})

        return dados
    

def gravar_modelos(veiculos):
    nome_arquivo = input("Nome do arquivo: ")

    with open(nome_arquivo, "w") as arquivo:
        for veiculo in veiculos:
            arquivo.write(f"{veiculo['nome']};{veiculo['montadora']};{veiculo['valor_referencia']};{veiculo['motorizacao']};{veiculo['turbo']};{veiculo['automatico']}\n")

    print("Dados gravados com sucesso!")


def remover_modelo(modelos):
    """Lista veículos e remove com base no ID do veículo"""

    listar_modelos(modelos)

    ID = input("ID do veículo: ")

    vetor_novo = [veiculo for veiculo in modelos if veiculo['id'] != ID]
    modelos.clear()
    modelos.extend(vetor_novo)

    return modelos

