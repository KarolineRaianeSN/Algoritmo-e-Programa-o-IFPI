'''
Leia o valor do raio de uma circunferência, calcule e escreva seu comprimento.(c = 2 * p * r)
'''
import math
#Entrada
raio = int(input(f'Digite o valor do raio: '))

#Processamento
area = 2 * raio * math.pi

#Saída
print(f'O valor do comprimento da circunferência é igual a {area:.2f}')