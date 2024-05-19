def main():
    N = int(input())

    for _ in range(N):
        X, Y = map(int, input().split())
        if X > Y:
            X, Y = Y, X
        soma = sum(i for i in range(X + 1 if X % 2 == 0 else X, Y + 1, 2))
        print(soma)


main()