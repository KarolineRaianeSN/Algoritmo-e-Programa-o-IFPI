"""
Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal.
"""

# Entrada
binario = int(input(f'Digite um número binário com 4 dígitos: '))

# Processamento
digito_4 = (binario // 1000) * 2**3
digito_3 = (binario % 1000) // 100 * 2**2
digito_2 = (binario % 100) // 10 * 2**1
digito_1 = (binario % 10)

soma = digito_4 + digito_3 + digito_2 + digito_1

# Saída
print(f'O número {binario} equivale a {soma} na base decimal')
