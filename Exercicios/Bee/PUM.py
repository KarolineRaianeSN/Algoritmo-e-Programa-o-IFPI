def main():
    N = int(input())

    inicio = 1

    while N > 0:
        print(inicio, inicio + 1, inicio + 2, "PUM")
        inicio += 4
        N -= 1


main()