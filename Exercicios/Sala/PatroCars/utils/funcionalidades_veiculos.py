from utils.funcionalidades import *
from utils.menus import *
from utils.ulid import gerar_ulid 
from montadoras import lista_montadoras
from modelos import lista_modelos
import pprint


def adicionar_veiculo(veiculos: list):
    """Lista montadoras e modelos e pede ao usuários para escolher montadora e modelo, pede os dados e adiciona na lista"""

    limpar_tela()

    if not lista_montadoras:
        print("Nenhuma montadora cadastrada. Cadastre uma montadora primeiro.")
        return 
    
    if not lista_modelos:
        print("Nenhum modelo cadastrado. Cadastre um modelo primeiro.")
        return
    
    print("=================== MONTADORAS CADASTRADAS ===================")
    for i, montadora in enumerate(lista_montadoras):
        print(f"{i + 1}. {montadora['nome']}")
    
    escolha = int(input("Digite o número da montadora: ")) - 1
    montadora_selecionada = lista_montadoras[escolha]

    print("=================== MODELOS CADASTRADOS ===================")
    for i, modelo in enumerate(lista_modelos):
        print(f"{i + 1}. {modelo['nome']}")

    escolha = int(input("Digite o número do modelo: ")) - 1
    modelo_selecionado = lista_modelos[escolha]


    # (id: ULID, modelo_id: string, cor: string, ano_fabricacao: number, ano_modelo: number, valor: number, placa: string, vendido: boolean)

    nome = input("Nome do veículo: ")
    cor = input("Cor: ")
    ano_fabricacao = int(input("Ano de fabricação: "))
    ano_modelo = int(input("Ano do modelo: "))
    valor = float(input("Valor: "))
    placa = input("Placa: ")
    vendido = bool(int(input("Vendido (1: sim | 0: nao): ")))
    
    veiculos.append({
        'id': gerar_ulid(),
        'montadora': montadora_selecionada,
        'modelo': modelo_selecionado,
        'nome': nome,
        'cor': cor,
        'ano_fabricacao': ano_fabricacao,
        'ano_modelo': ano_modelo,
        'valor': valor,
        'valor_referencia': valor_modelo,
        'placa': placa,
        'vendido': vendido
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


def ordenar_veiculos(veiculos: list):
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


def encontrar_veiculos(veiculos) -> list:
    """Encontra veículo e imprime na tela"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    opcao = input(filtros_veiculos())  # Exibe os filtros disponíveis

    match opcao:
        case "1":
            limpar_tela()
            for veiculo in veiculos:
                print(veiculo["nome"])

            nome = input("Nome do veículo: ").strip().lower()
            filtro = lambda veiculo: nome in veiculo.get("nome", "").strip().lower()
        case "2":
            for montadora in lista_montadoras:
                print(montadora["nome"])
            montadora = input("Montadora do veículo: ").strip().lower()
            # Verifica se montadora é uma string ou um dicionário
            filtro = lambda veiculo: montadora in (
                veiculo.get("montadora", {}).get("nome", "").strip().lower() if isinstance(veiculo.get("montadora"), dict)
                else veiculo.get("montadora", "").strip().lower()
            )
        case "3":
            modelo = input("Modelo do veículo: ").strip().lower()
            filtro = lambda veiculo: modelo in veiculo.get("modelo", {}).get("nome", "").strip().lower()
        case "4":
            ano_fabricacao = input("Ano de fabricação: ").strip()
            filtro = lambda veiculo: str(veiculo.get("ano_fabricacao", "")).strip() == ano_fabricacao
        case "5":
            ano_modelo = input("Ano de modelo: ").strip()
            filtro = lambda veiculo: str(veiculo.get("ano_modelo", "")).strip() == ano_modelo
        case "6":
            placa = input("Placa do veículo: ").strip().lower()
            filtro = lambda veiculo: veiculo.get("placa", "").strip().lower() == placa
        case "7":
            vendido = input("Vendido (1: sim | 2: nao): ").strip()
            vendido_bool = vendido == '1'
            filtro = lambda veiculo: veiculo.get("vendido", False) == vendido_bool
        case "0":
            limpar_tela()
            return
        case _:
            print("Opção inválida")
            return

    veiculos_encontrados = list(filter(filtro, veiculos))

    if veiculos_encontrados:
        listar_veiculos(veiculos_encontrados)
    else:
        print("Nenhum veículo encontrado.")





def atualizar_veiculos(veiculos):
    """Atualiza veículo na lista de acordo com critério escolhido"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    # Encontra veículos com base nos critérios do usuário
    veiculos_encontrados = encontrar_veiculos(veiculos)

    if not veiculos_encontrados:
        print("Nenhum veículo encontrado.")
        return veiculos  # Não modifica a lista original se não encontrar veículos

    opcao = input(menu_atualizar_veiculos(veiculos_encontrados))

    # Verifica se o usuário deseja realmente atualizar algo
    if opcao == "0":
        return veiculos  # Sai sem modificar a lista

    # Atualiza de acordo com a opção do usuário
    match opcao:
        case "1":
            nome_atual = input("Nome atual do veículo: ").strip().lower()
            novo_nome = input("Novo nome do veículo: ").strip().lower()
            for veiculo in veiculos_encontrados:
                if nome_atual == veiculo["nome"].strip().lower():
                    veiculo["nome"] = novo_nome
        case "2":
            modelo_atual = input("Modelo atual do veículo: ").strip().lower()
            novo_modelo = input("Novo modelo do veículo: ").strip().lower()
            for veiculo in veiculos_encontrados:
                if modelo_atual == veiculo["modelo"]["nome"].strip().lower():
                    veiculo["modelo"]["nome"] = novo_modelo
        case "3":
            cor_atual = input("Cor atual do veículo: ").strip().lower()
            nova_cor = input("Nova cor do veículo: ").strip().lower()
            for veiculo in veiculos_encontrados:
                if cor_atual == veiculo["cor"].strip().lower():
                    veiculo["cor"] = nova_cor
        case "4":
            ano_fabricacao_atual = int(input("Ano de fabricação atual do veículo: "))
            novo_ano_fabricacao = int(input("Novo ano de fabricação do veículo: "))
            for veiculo in veiculos_encontrados:
                if ano_fabricacao_atual == veiculo["ano_fabricacao"]:
                    veiculo["ano_fabricacao"] = novo_ano_fabricacao
        case "5":
            ano_modelo_atual = int(input("Ano de modelo atual do veículo: "))
            novo_ano_modelo = int(input("Novo ano de modelo do veículo: "))
            for veiculo in veiculos_encontrados:
                if ano_modelo_atual == veiculo["ano_modelo"]:
                    veiculo["ano_modelo"] = novo_ano_modelo
        case "6":
            placa_atual = input("Placa atual do veículo: ").strip().lower()
            nova_placa = input("Nova placa do veículo: ").strip().lower()
            for veiculo in veiculos_encontrados:
                if placa_atual == veiculo["placa"].strip().lower():
                    veiculo["placa"] = nova_placa
        case "7":
            vendido_atual = input("Vendido atual do veículo (1: sim | 2: nao): ")
            novo_vendido = input("Novo status (1: sim | 2: nao): ")
            for veiculo in veiculos_encontrados:
                veiculo["vendido"] = True if novo_vendido == "1" else False
        case _:
            print("Opcão inválida")
            return atualizar_veiculos(veiculos)

    print("Veículo(s) atualizado(s) com sucesso!")
    return veiculos  # Retorna a lista atualizada



def remover_veiculos(veiculos: list):
    """Remove veículo de acordo com id do veículo"""

    if not veiculos:
        print("Nenhum veículo cadastrado.")
        return veiculos

    listar_veiculos(veiculos)

    id_veiculo = input("ID do veículo: ").strip()

    # Verifica se algum veículo foi removido
    veiculos_filtrados = [veiculo for veiculo in veiculos if veiculo["id"] != id_veiculo]

    if len(veiculos_filtrados) == len(veiculos):
        print("Veículo com o ID informado não foi encontrado.")
    else:
        veiculos[:] = veiculos_filtrados  # Atribuição direta à lista original
        print("Veículo removido com sucesso.")

    return veiculos



def carregar_veiculos(veiculos):
    """Carrega veículos de um arquivo"""

    arquivo = input("Nome do arquivo: ")

    try:
        with open(arquivo, "r") as arquivo:
            chaves = ['id', 'montadora', 'modelo', 'nome', 'cor', 'ano_fabricacao', 'ano_modelo', 'valor', 'valor_referencia', 'placa', 'vendido']

            veiculos.clear()  # Clear the list here

            for linha in arquivo:
                veiculos.append(dict(zip(chaves, linha.strip().split(';'))))

    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return carregar_veiculos()

def gravar_veiculos(veiculos: list):
    """Grava veículos em um arquivo"""

    arquivo = input("Nome do arquivo: ")

    with open(arquivo, "w") as arquivo:
        for veiculo in veiculos:
            arquivo.write(f"{veiculo['id']};{veiculo['nome']};{veiculo['modelo']};{veiculo['cor']};{veiculo['ano_fabricacao']};{veiculo['ano_modelo']};{veiculo['placa']};{veiculo['vendido']}\n")

    print("Dados gravados com sucesso!")