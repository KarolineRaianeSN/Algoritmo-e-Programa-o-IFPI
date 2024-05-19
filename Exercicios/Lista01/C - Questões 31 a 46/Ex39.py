"""
Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão: D = (R + S)/2, onde R = (A + B)**2 e S = (B + C)**2
"""
# Entrada
A = int(input(f'Digite o valor de A: '))
B = int(input(f'Digite o valor de B: '))
C = int(input(f'Digite o valor de C: '))

# Processamento
R = (A + B)**2
S = (B + C)**2
D = (R + S) / 2

# Saída
print(f'D = (R + S)/2 é igual a {D}')