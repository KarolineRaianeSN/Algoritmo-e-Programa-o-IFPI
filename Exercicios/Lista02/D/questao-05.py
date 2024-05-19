"""
Leia 3 (três) números e escreva-os em ordem crescente.
"""


def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    comparacao(numero1, numero2, numero3)


def comparacao(numero1, numero2, numero3):
    menor = 0
    meio = 0
    maior = 0
    if numero1 <= numero2 and numero1 <= numero3:
        menor = numero1
    elif numero2 <= numero1 and numero2 <= numero3:
        menor = numero2
    else:
        menor = numero3

        # Encontrar o maior número
    if numero1 >= numero2 and numero1 >= numero3:
        maior = numero1
    elif numero2 >= numero1 and numero2 >= numero3:
        maior = numero2
    else:
        maior = numero3

        # Encontrar número do meio
    meio = numero1 + numero2 + numero3 - maior - menor

    print(f"Os números em ordem crescente são: {menor}, {meio} e {maior}")


if __name__ == "__main__":
    main()
