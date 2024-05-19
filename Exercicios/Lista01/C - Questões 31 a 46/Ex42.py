"""
Escreva um algoritmo que, tendo como dados de entrada 2 pontos quaisquer no plano, ponto1 (x1,y1) e ponto2 (x2,y2),
escreva a distância entre eles, conforme fórmula abaixo.
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
"""
import math
# Entrada
x1 = int(input(f'Digite o valor de x1: '))
y1 = int(input(f'Digite o valor de y1: '))
x2 = int(input(f'Digite o valor de x2: '))
y2 = int(input(f'Digite o valor de y2: '))

# Processamento
d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Saída
print(f'A distância entre os pontos ({x1},{y1}) e ({x2},{y2}) é igual a {d}')