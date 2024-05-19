"""
Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
formadas pelos seus dois primeiros e dois últimos dígitos.
Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.
"""
import math
def main():

    numero = int(input("Digite um número de 4 dígitos: "))

    calc_quadrado(numero)
def calc_quadrado(numero):
    numero_str = str(numero)
    primeiro_par = int(numero_str[:2])
    segundo_par = int(numero_str[2:])
    if primeiro_par + segundo_par == math.sqrt(numero):
        return print("O número é um quadrado perfeito")
    else:
        return print("O número não é um quadrado perfeito")



if __name__ == "__main__":
    main()