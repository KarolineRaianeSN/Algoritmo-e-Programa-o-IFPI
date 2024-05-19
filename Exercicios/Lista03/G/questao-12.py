"""
Leia um número e escreva se o número é inteiro ou decimal.
"""


def main():

    numero = float(input("Digite um número: "))
    resultado = inteiro_decimal(numero)
    print(f"O número é {resultado}")


def inteiro_decimal(numero):
    if numero == round(numero):
        return "inteiro"
    else:
        return "decimal"


if __name__ == "__main__":
    main()