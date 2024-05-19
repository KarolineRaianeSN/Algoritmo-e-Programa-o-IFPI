"""
Leia 1 (um) número inteiro e escreva se este número é par ou impar.
"""
def main():
    numero = int(input("Digite um número: "))

    par_ou_impar(numero)

    
def par_ou_impar(numero):
    if numero % 2 == 0:
        return print("É um número par")
    else:
        return print ("É um numero ímpar")

if __name__ == "__main__":
    main()