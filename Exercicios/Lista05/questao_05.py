"""Leia um número, calcule e escreva seu fatorial."""
def main():

    numero = int(input("Digite um número para determinar o fatorial: "))

    fatorial = 1

    for i in range(1,numero):
        fatorial += fatorial * i

    print(fatorial)

main()