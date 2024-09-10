"""
Entrada
A entrada consiste de diversos casos de teste, cada um em uma linha. Cada linha contém dois inteiros D e N (1 ≤ D ≤ 9, 1 ≤ N < 10100 ), representando, respectivamente, o dígito que está apresentando problema na máquina e o número que foi negociado originalmente no contrato (que podem ser grande, pois Modernolândia tem sido acometida por hiperinflação nas últimas décadas).

O ultimo caso de teste é seguido por uma linha que contém apenas dois zeros separados por espaços em branco.

Saída
Para cada caso de teste da entrada o seu programa deve imprimir uma linha contendo um único inteiro V, o valor numérico representado de fato no contrato.
"""
def main():
    d,n = input().split()

    if is_digit(d, n):
        while d and n != '0':
            valor_errado = ''
            for digito in n:
                if digito == d:
                    continue
                else:
                    valor_errado += digito
            

            print(int(valor_errado))
            d,n = input().split()

def is_digit(digito, valor):
    return digito.isdigit() and valor.isdigit()


main()