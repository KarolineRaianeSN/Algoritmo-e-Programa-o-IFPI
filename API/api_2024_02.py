def main():

    numero = int(input("Digite um número:"))
    eh_numero(numero)

def eh_numero(numero):
    num = numero.isdigit()
    if num == True:
        return numero
    else:
        numero = int(input())

main()