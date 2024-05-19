"""
Leia um número de 01 a 100, verifique e escreva se o número é o não primo.
"""

def main():
    numero = int(input("Digite um número de 01 a 100: "))
    verificacao_primo(numero)

def verificacao_primo(numero):
    if numero == 1:
        return print("Não é um número primo")
    elif numero == 0:
        return print("Não é um número primo")
    elif numero == 2:
        return print("É um número primo")
    elif numero > 2:
        for i in range  (2,numero):
            if numero % i == 0:
                return print(f"O número {numero} não é primo")
            else:
                return print(f"O número {numero} é primo")




if __name__ == "__main__":
    main()