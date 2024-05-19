"""
Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).
"""


def main():

    angulo1 = int(input("Digite o primeiro ângulo: "))
    angulo2 = int(input("Digite o segundo ângulo: "))
    angulo3 = int(input("Digite o segundo ângulo: "))

    if forma_triangulo(angulo1, angulo2, angulo3):
        print("Forma um triângulo")
        classificacao(angulo1, angulo2, angulo3)
        print(f"Forma um triângulo {classificacao(angulo1, angulo2, angulo3)}")
    else:
        print("Não forma um triângulo")


def forma_triangulo(angulo1,angulo2,angulo3):
    return angulo1 + angulo2 + angulo3 == 180


def classificacao(angulo1,angulo2,angulo3):
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return "acutângulo"
    elif angulo1 == 90 or angulo2 == 90 or angulo3 == 90:
        return "retângulo"
    else:
        return "obtusângulo"


if __name__ == "__main__":
    main()
