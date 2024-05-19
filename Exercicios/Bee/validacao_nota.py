def main():
    notas = []
    count = 0

    while count < 2:
        nota = float(input())
        if 0 <= nota <= 10:
            notas.append(nota)
            count += 1
        else:
            print("nota invalida")

    media = sum(notas) / 2
    print("media = {:.2f}".format(media))


if __name__ == '__main__':
    main()