def main():
    X = int(input())
    Y = int(input())

    soma_impares = 0

    if X < Y:
        atual = X + 1 if X % 2 == 0 else X + 2
        while atual < Y:
            soma_impares += atual
            atual += 2
    else:
        atual = Y + 1 if Y % 2 == 0 else Y + 2
        while atual < X:
            soma_impares += atual
            atual += 2

    print(soma_impares)

main()