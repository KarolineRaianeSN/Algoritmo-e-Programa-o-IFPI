"""
Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou
quarto) em que o ângulo se localiza.
"""
def main():
    angulo = int(input("Digite o valor de um ângulo: "))
    classificacao_angulo = classificacao(angulo)
    print(f"O seu angulo está localizado no {classificacao_angulo}")


def classificacao(angulo):
    if angulo <= 90:
        return "quadrante 1"
    elif angulo <= 180:
        return "quarante 2"
    elif angulo <= 270:
        return "quadrante 3"
    elif angulo < 360:
        return "quadrante 4"
    else:
        return "quadrante inválido"


if __name__ == "__main__":
    main()