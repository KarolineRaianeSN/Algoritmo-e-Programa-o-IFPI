def main():

    N = int(input())

    dentro_intervalo = 0
    fora_intervalo = 0

    i = 0
    while i < N:

        X = int(input())

        if 10 <= X <= 20:
            dentro_intervalo += 1
        else:
            fora_intervalo += 1

        i += 1

    print(f"{dentro_intervalo} in")
    print(f"{fora_intervalo} out")


main()