

def main():

    n = int(input("Digite um número: "))

    digitos = contar_digitos(n)

    print(f"O número {n} tem {digitos} dígitos.")

def contar_digitos(n):
    cont = 0
    while n != 0:
        n //= 10
        cont += 1
    return cont


main()
