def main():
    while True:
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

        while True:
            print("novo calculo (1-sim 2-nao)")
            opcao = int(input())
            if opcao == 1 or opcao == 2:
                break
        if opcao == 2:
            break


if __name__ == '__main__':
    main()