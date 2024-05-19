def main():
    alcool = 0
    gasolina = 0
    diesel = 0

    while True:
        codigo = int(input())

        if codigo == 4:
            break

        if codigo == 1:
            alcool += 1
        elif codigo == 2:
            gasolina += 1
        elif codigo == 3:
            diesel += 1
        else:
            continue

    print("MUITO OBRIGADO")
    print("Alcool:", alcool)
    print("Gasolina:", gasolina)
    print("Diesel:", diesel)


main()