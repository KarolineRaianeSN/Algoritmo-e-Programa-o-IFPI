"""Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
numero de identificação e o peso do boi mais magro e do boi mais gordo."""
def main():

    fichas = int(input("Número de fichas: "))

    maior_peso = 0
    nome_maior_peso = ""
    for i in range(fichas):
        id = int(input("Número de identificação: "))
        nome = input("Nome: ")
        peso = int(input("Peso (em kg): "))

        if peso > maior_peso:
            maior_peso = peso
            nome_maior_peso = nome
    print(f"""
    ---- BOI DE MAIOR PESO ----
    Nome: {nome_maior_peso}
    Peso: {maior_peso} Kg
    ----------------------------""")

main()