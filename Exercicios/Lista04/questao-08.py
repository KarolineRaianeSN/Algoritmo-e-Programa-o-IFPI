"""Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo
quando a soma de dois números consecutivos da lista for igual a X
"""


def main():

    x = int(input("Digite um número x: "))


    numero1 = int(input("Digite um número: "))
    numero2 = int(input("Digite um número: "))

    numeros = [numero1, numero2]

    n1 = numeros[-2]
    n2 = numeros[-1]

    soma = n1 + n2
    while soma != x:
        numero = int(input("Digite mais um número: "))
        numeros.append(numero)

        soma = n2 + numero

    print("Fim")

main()