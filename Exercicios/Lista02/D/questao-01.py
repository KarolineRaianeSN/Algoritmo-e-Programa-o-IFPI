"""
Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.
"""


def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    comparacao(numero1, numero2, numero3)


def comparacao(numero1,numero2,numero3):
    if numero1 == numero2 == numero3:
        return print("Há 3 números iguais")
    elif numero1 == numero2 or numero1 == numero3 or numero2 == numero3:
        return print("Há 2 números iguais")
    else:
        return print("Não há números iguais")


if __name__ == "__main__":
    main()
