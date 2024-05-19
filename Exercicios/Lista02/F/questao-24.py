"""
Leia os coeficientes (A, B e C) de uma equação de 2° grau e escreva suas raízes. Vale lembrar que o
coeficiente A deve ser diferente de 0 (zero).
"""
import math


def main():
    a = int(input("Digite o coeficiente a: "))
    b = int(input("Digite o coeficiente B: "))
    c = int(input("Digite o coeficiente C: "))

    raizes(a, b, c)


def calc_delta(a, b, c):
    if a == 0:
        raise Exception("Coeficiente inválido")
    return b ** 2 - 4 * (a * c)


def raizes(a, b, c):
    delta = calc_delta(a, b, c)
    print(delta)
    if delta < 0:
        return print("Nenhuma raiz")
    raiz = math.sqrt(delta)
    x1 = ((b * -1) + raiz) / (2 * a)
    x2 = ((b * -1) - raiz) / (2 * a)
    return print(f"As raízes da equação são: {x1} e {x2}")


if __name__ == "__main__":
    main()
