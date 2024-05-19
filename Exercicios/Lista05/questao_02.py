"""Leia N e escreva todos os números inteiros pares de 1 a N."""
def main():

    numero = int(input("Digite um número: "))

    for i in range(1,numero + 1):
        if i % 2 != 0:
            continue
        else:
            print(i)

main()