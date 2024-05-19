def main():
    nome = input("Nome: ")
    peso = int(input("Peso: "))
    altura = float(input("Altura: "))

    nome_maior = nome
    peso_maior = peso
    nome_menor = nome
    peso_menor = peso


    peso_menor = peso

    while nome != "Fim":
        if peso >  peso_maior:
            peso_maior = peso
            nome_maior = nome
        if peso < peso_menor:
            peso_menor = peso
            nome_menor = nome

        nome = input("Nome: ")
        if nome == "Fim":
            print("Programa encerrado")
        else:
            peso = int(input("Peso: "))
            altura = float(input("Altura: "))

    resultado = f"""Modelo com menor peso:
                    Nome: {nome_menor}
                    Peso: {peso_menor}
                    
                    Modelo com maior peso:
                    Nome: {nome_maior}
                    Peso: {peso_maior}"""

    print(resultado)


main()