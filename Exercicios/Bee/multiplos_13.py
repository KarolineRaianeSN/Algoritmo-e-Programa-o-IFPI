def main():
    X, Y = map(int, input().split())

    soma = 0

    if X > Y:
        X, Y = Y, X

    while X <= Y:
        if X % 13 != 0:
            soma += X
        X += 1

    print(soma)


if __name__ == '__main__':
    main()