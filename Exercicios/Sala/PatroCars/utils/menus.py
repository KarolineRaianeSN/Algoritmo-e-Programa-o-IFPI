def menu_principal():
    """Menu principal"""
    texto_menu = f"""
============== MONTADORAS ==============
1. Gerenciar montadoras
2. Gerenciar modelos de veículos
3. Gerenciar veículos
0. Sair
========================================

Escolha uma opção: """

    return texto_menu


def menu_montadoras():
    """Menu montadoras"""
    texto_menu = f"""
======  GERENCIAR MONTADORAS ===============
1. Adicionar montadora
2. Listar montadoras
3. Filtrar montadoras
4. Atualizar montadora
5. Remover montadora
6. Carregar dados de arquivo
7. Gravar dados em arquivo
0. Sair
============================================

Escolha uma opção: """

    return texto_menu

def filtros_montadoras():
    """Tipos de filtragem para encontrar montadora"""
    texto_menu = f"""
======  FILTRAR MONTADORAS ===============
1. Por nome
2. Por país
3. Por ano de fundação
0. Voltar
============================================

Escolha uma opção: """

    return texto_menu


def menu_atualizar_montadora():
    """Menu atualizar montadora"""
    texto_menu = f"""
======  ATUALIZAR MONTADORA ===============
1. Nome
2. País
3. Ano de fundação
4. Todas as informações
0. Voltar
============================================

Escolha uma opção: """

    return texto_menu


def menu_modelos():
    """Menu veículos"""
    texto_menu = f"""
======  GERENCIAR MODELOS ===============
1. Adicionar modelo
2. Listar modelos
3. Filtrar modelos
4. Atualizar modelos
5. Remover modelo
6. Carregar dados de arquivo
7. Gravar dados em arquivo
0. Sair
============================================

Escolha uma opção: """

    return texto_menu


def filtros_modelos():
    """Tipos de filtragem para encontrar veiculo"""
    texto_menu = f"""
======  FILTRAR VEICULOS ===============
1. Por nome
2. Por montadora
3. Por valor de referência
4. Por motoração
5. Por turbo
6. Por automação
0. Voltar
============================================

Escolha uma opção: """

    return texto_menu


def menu_atualizar_modelos(veiculos):
    """Menu atualizar veiculo"""
    texto_menu = f"""
======  ATUALIZAR VEICULO ===============
1. Nome
2. Montadora
3. Valor de referência
4. Motoração
5. Turbo
6. Automação
7. Tudo
0. Voltar
============================================

Escolha uma opção: """

    return texto_menu


def menu_veiculos():
    """Menu veiculos"""
    texto_menu = f"""
======  GERENCIAR VEICULOS ===============
1. Adicionar veiculo
2. Listar veiculos
3. Filtrar veiculos
4. Atualizar veiculo
5. Remover veiculo
6. Carregar dados de arquivo
7. Gravar dados em arquivo
0. Sair
============================================

Escolha uma opção: """

    return texto_menu


def filtros_veiculos():
    """Tipos de filtragem para encontrar veiculo"""
    texto_menu = f"""
======  FILTRAR VEICULOS ===============
1. Por nome
2. Por montadora
3. Por valor de referência
4. Por motoração
5. Por turbo
6. Por automação
0. Voltar
============================================

Escolha uma opção: """

    return texto_menu


def menu_atualizar_veiculos(veiculos):
    # (id: ULID, modelo_id: string, cor: string, ano_fabricacao: number, ano_modelo: number, valor: number, placa: string, vendido: boolean)
    """Menu atualizar veiculo"""
    texto_menu = f"""
======  ATUALIZAR VEICULO ===============
1. Nome
2. Modelo
3. Cor
4. Ano de fabricação
5. Ano de modelo
6. Valor de referência
7. Placa
8. Vendido
9. Tudo
0. Voltar
============================================

Escolha uma opção: """

    return texto_menu