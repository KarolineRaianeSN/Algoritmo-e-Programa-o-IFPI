import math


def main():
    valores_x = input()
    valores_y = input()

    x = valores_x.split(" ")
    y = valores_y.split(" ")

    x1 = float(x[0])
    y1 = float(x[1])
    x2 = float(y[0])
    y2 = float(y[1])

    distancia = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

    print(f"{distancia:.4f}")


main()