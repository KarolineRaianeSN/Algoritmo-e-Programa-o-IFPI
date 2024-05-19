"""
Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.
"""
def main():

    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    minimo = min(numero1, numero2)

    while not (calc_mmc(minimo, numero1) and calc_mmc(minimo, numero2)):
        minimo += 1

    print(f"O mmc entre {numero1} e {numero2} é igual a {minimo}")


def calc_mmc(valor1,valor2):
    return valor1 % valor2 == 0
main()