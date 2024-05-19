"""
Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.
"""
import math


def main():
    numero = int(input("Digite um número entre 1000 e 9999: "))

    calc_quadrado(numero)
def calc_quadrado(numero):
    numero_str = str(numero)
    primeiro_par = int(numero_str[:2])
    segundo_par = int(numero_str[2:])

    terceiro = primeiro_par + segundo_par
    if numero == terceiro **2:
        return print("O número obedece à regra")
    else:
        return print("O número não obedece à regra")



if __name__ == "__main__":
    main()