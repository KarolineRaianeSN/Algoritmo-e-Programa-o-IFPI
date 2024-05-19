"""Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...)."""
def main():

    numero = int(input("Digite um número N: "))

    sequencia = 0

    for i in range(1, numero + 1):
        sequencia += i
        print(sequencia)


main()