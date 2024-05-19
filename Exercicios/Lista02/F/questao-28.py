"""
Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de
um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área
não pode ser negativo.
"""


def main():
    x1 = int(input("Leia a coordenada x1: "))
    x2 = int(input("Leia a coordenada x2: "))
    y1 = int(input("Leia a coordenada y1: "))
    y2 = int(input("Leia a coordenada y2: "))

    calc_area(x1, x2, y1, y2)


def calc_area(x1, x2, y1, y2):
    area = abs(x2 - x1) * abs(y2 - y1)
    print(f"O valor da área é igual a {area}")


if __name__ == "__main__":
    main()
