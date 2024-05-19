def main():

    numero = int(input("Digite um número: "))

    binario = calc_binario(numero)
    hexa = calc_hexa(numero)

    print(f"Binário: {binario} | Hexadecimal: {hexa}")

def calc_binario(numero):
    binario = ""
    while numero > 0:
        binario = str(numero % 2) + binario
        numero = numero // 2

    return binario


def calc_hexa(numero):
    hexa = ""
    while numero > 0:
        digito = numero % 16

        if digito == 10:
            digito = "A"
        elif digito == 11:
            digito = "B"
        elif digito == 12:
            digito = "C"
        elif digito == 13:
            digito = "D"
        elif digito == 14:
            digito = "E"
        elif digito == 15:
            digito = "F"

        hexa = str(digito) + hexa
        numero = numero // 16

    return hexa


main()