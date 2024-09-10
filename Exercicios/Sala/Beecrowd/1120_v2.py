"""
Entrada
A entrada consiste de diversos casos de teste, cada um em uma linha. Cada linha contém dois inteiros D e N (1 ≤ D ≤ 9, 1 ≤ N < 10100 ), representando, respectivamente, o dígito que está apresentando problema na máquina e o número que foi negociado originalmente no contrato (que podem ser grande, pois Modernolândia tem sido acometida por hiperinflação nas últimas décadas).

O ultimo caso de teste é seguido por uma linha que contém apenas dois zeros separados por espaços em branco.

Saída
Para cada caso de teste da entrada o seu programa deve imprimir uma linha contendo um único inteiro V, o valor numérico representado de fato no contrato.
"""
def main():
    d,n = is_digit()

    while d and n != '0':
        valor_errado = n.replace(d, '')
        valor_errado = int(valor_errado) if valor_errado.isdigit() else 0
        print(valor_errado)

        d,n = is_digit()

def is_digit():
    d, n = input("Digite um valor: ").split()
    if d.isdigit() and n.isdigit():
        return d, n
    return is_digit()

main()