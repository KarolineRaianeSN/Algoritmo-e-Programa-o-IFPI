"""Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
(0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2."""
def main():

    numero = int(input("Digite o número de termos que deseja da sequência de Fibonacci: "))

    if numero < 2:
        print("Número inválido")
        numero = int(input("Digite o número de termos que deseja da sequência de Fibonacci: "))

    primeiro_termo = 0
    segundo_termo = 1
    print(primeiro_termo)
    print(segundo_termo)

    for i in range(2,numero):
        terceiro_termo = primeiro_termo + segundo_termo
        print(terceiro_termo)
        primeiro_termo = segundo_termo
        segundo_termo = terceiro_termo

main()