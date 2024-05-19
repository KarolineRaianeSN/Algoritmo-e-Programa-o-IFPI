"""Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista."""
def main():

    numero = int(input("Digite um número: "))

    resultado = 0

    for i in range(numero + 1):
        resultado += i
    media = resultado / numero
    print(f"Soma = {resultado} Média = {media}")

main()