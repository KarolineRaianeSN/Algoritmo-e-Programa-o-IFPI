"""
Um sistema de equações lineares do tipo , pode ser resolvido segundo mostrado abaixo:

Escreva um algoritmo que leia os coeficientes a, b, c, d, e e f, calcule e escreva os valores de x e y.
"""
print(f'Leve em conta a equação linear do tipo: ax + by = c e dx + ey = f, digite os valores de a,b,c,d,e e f')
# Entrada
a = int(input(f'Digite o valor de a: '))
b = int(input(f'Digite o valor de b: '))
c = int(input(f'Digite o valor de c: '))
d = int(input(f'Digite o valor de d: '))
e = int(input(f'Digite o valor de e: '))
f = int(input(f'Digite o valor de f: '))

# Processamento
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)

# Saída
print(f'O valor de x é igual a {x} e o valor de y é igual a {y}')