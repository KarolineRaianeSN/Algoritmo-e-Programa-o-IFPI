def main():
    maior = 0
    posicao = 0
    i = 1

    while i <= 100:
        valor = int(input())
        if valor > maior:
            maior = valor
            posicao = i
        i += 1

    print(maior)
    print(posicao)


if __name__ == '__main__':
    main()