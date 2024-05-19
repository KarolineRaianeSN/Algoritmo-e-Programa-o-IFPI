def main():

    n = int(input("Digite o valor de n: "))
    x = int(input("Digite o valor de x: "))

    resultado = divisoes(n, x)


def divisoes(n, x):
    while n >= 2:
        x = x / n
        n = n - 1
        print("X / N = ", x)

main()