"""
Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.
"""


def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    maior(numero1,numero2)


def maior(numero1,numero2):
    if numero2 > numero1:
        return print(f"O número {numero2} é o maior número")
    elif numero1 > numero2:
        return print(f"O número {numero1} é o maior número")
    else:
        return print("Os números são iguais")


if __name__ == "__main__":
    main()
