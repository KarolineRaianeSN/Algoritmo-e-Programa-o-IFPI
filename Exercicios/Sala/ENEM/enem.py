from pprint import pprint

"""Sugestões de consultas:
Top N Brasil (todas as áreas)
Top N Brasil por Área
Top N por Estado
Top N por Estado e Rede (pública ou privada)
Media Nacional por Área
Melhor escola por Área e Estado ou BR
Listas Escolas por Estado Ordenada Por Renda
Busca escola específica por parte  Nome
Ranking ENEM por Estado
Ranking ENEM por Região do País

arquivo: enem2014_nota_por_escola.txt.csv
"""
def main():
    nome_arquivo = input("Nome do arquivo: ")
    ler_arquivo(nome_arquivo)


def ler_arquivo(arquivo):
    """Lê arquivo e salva os dados em um dicionário"""

    with open(arquivo, 'r', encoding="utf-8", errors='ignore') as file:
        # cabecalho
        header = ["ranking", "nome", "municipio", "uf", "rede", "permanencia", "renda", "media_objetivas", 
                "linguagens", "matematica", "natureza", "humanas", "redacao"]

        dados = [dict(zip(header, linha.strip().split(";"))) for linha in file]

        pprint(dados)


main()