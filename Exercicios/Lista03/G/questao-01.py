"""
Leia um número e mostre na tela se o número é positivo ou negativo.
"""
def main():

    numero = int(input("Digite um número: "))

    positivo_negativo(numero)
def positivo_negativo(numero):
    if numero > 0:
        return print("É um número positivo")
    else:
        return print("É um número negativo")

if __name__ == "__main__":
    main()