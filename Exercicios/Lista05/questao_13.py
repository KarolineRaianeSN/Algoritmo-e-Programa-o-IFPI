"""Leia N e uma lista de N números e escreva o maior número da lista."""
def main():

    numero = int(input("Digite a quantidade de números: "))
    maior_numero = 0

    for i in range(numero):
        digito = int(input("Digite um número para a lista: "))
        if numero > maior_numero:
            maior_numero = digito

    print(f"Maior número é igual a: {maior_numero}")



main()