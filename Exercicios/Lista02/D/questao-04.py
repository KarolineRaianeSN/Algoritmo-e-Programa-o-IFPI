"""
Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual ou diferente
do algarismo da unidade.
"""


def main():
    numero = int(input("Digite um número com 2 dígitos: "))

    calcular_maior_digito(numero)


def calcular_maior_digito(numero):
    dezena = numero // 10
    unidade = numero % 10

    if dezena == unidade:
        return print("Os algorismo da dezena é igual ao algorismo da unidade ")
    else:
        return print("Os algorismos são diferentes")


if __name__ == "__main__":
    main()
