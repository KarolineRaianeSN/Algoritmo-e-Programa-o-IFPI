"""
Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:
número = 9534 ; soma = 9+5+3+4 = 21.
"""
# Entrada
numero = int(input(f'Digite um número com 4 dígitos: '))

# Processamento
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10
soma = milhar + centena + dezena + unidade

# Saída
print(f'A soma entre {milhar}, {centena}, {dezena} e {unidade} é igual a {soma}')

