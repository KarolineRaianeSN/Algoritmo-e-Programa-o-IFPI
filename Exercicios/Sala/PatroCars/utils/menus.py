def menu_principal_v1():
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