def main():

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))


    mdc = calc_mdc(numero1,numero2)


    print(f"O mdc entre {numero1} e {numero2} é {mdc}")


def calc_mdc(numero1, numero2):
    while numero2 != 0:
        numero1, numero2 = numero2, numero1 % numero2
        return numero1

main()