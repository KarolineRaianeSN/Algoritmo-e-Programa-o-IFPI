"""Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido."""
def main():

    numero = int(input("Digite um número: "))

    resultado = 0

    for i in range(numero + 1):
        resultado += i
    print(resultado)

main()