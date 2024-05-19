'''
Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r3) / 3) (p = 3,14)
'''
import math
#Entrada
raio = int(input(f'Digite o valor do raio: '))

#Processamento
volume = (4 * raio**3 * math.pi) / 3

#Saída
print(f'O valor do volume da esfera é igual a {volume:.2f}')