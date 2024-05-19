def main():

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado = 0

    while numero2 > 0:
        resultado += numero1

        numero2 -= 1

    print(resultado)

main()