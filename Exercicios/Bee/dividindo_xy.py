def main():
    N = int(input())

    i = 0

    while i < N:
        X, Y = map(int, input().split())
        if Y != 0:
            resultado = X / Y
            print("{:.1f}".format(resultado))
        else:
            print("divisao impossivel")
        i += 1


main()