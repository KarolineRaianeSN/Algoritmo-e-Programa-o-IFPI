""" Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o
resultado da última divisão efetuada."""
def main():

    numero = int(input("Digite um número: "))
    resultado = calc_divisoes(numero)
    print(resultado)

def calc_divisoes(numero):
    while numero >= 1:
        numero /= 2
    return numero

main()