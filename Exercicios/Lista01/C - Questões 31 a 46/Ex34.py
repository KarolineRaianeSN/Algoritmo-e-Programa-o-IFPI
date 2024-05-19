"""
Leia 3 números, calcule e escreva a média dos números.
"""
# Entrada
numero_1 = int(input(f'Digite o primeiro número: '))
numero_2 = int(input(f'Digite o segundo número: '))
numero_3 = int(input(f'Digite o terceiro número: '))

# Processamento
media = (numero_1 + numero_2 + numero_3) / 3

# Saída
print(f'A média entre {numero_1}, {numero_2} e {numero_3} é igual a {media}')