"""
Leia 3 (três) números, verifique e escreva o maior entre os números lidos.
"""


def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    comparacao(numero1,numero2,numero3)


def comparacao(numero1,numero2,numero3):
    if numero1 > numero2 and numero1 > numero2:
        return print(f"O maior número é igual a {numero1}")
    elif numero2 > numero1 and numero2 > numero3:
        return print(f"O maior número é igual a {numero2}")
    else:
        return print(f"O maior número é igual a {numero3}")


if __name__ == "__main__":
    main()
