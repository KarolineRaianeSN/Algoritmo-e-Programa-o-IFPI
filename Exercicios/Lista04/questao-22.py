"""Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores
de divisão (/ e %) sejam utilizados.
"""
def main():

    dividendo = int(input("Dividendo: "))
    divisor = int(input("Divisor: "))
    resto = dividendo
    quociente = 0

    while resto >= divisor:
        resto -= divisor
        quociente += 1

    resultado = f"A divisão de {dividendo} por {divisor} é igual a {quociente} com resto {resto}"
    print(resultado)
main()