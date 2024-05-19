"""Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
maior quadrado menor que 38 é 36 (quadrado de 6)."""
def main():

    numero = int(input("Digite o valor de N: "))

    for i in range(numero + 1):
        if i**2 <= numero:
            maior_quadrado = i**2
    print(maior_quadrado)

main()