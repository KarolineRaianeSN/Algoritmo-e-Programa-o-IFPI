"""
Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.
(Ex.: número = 532 ; inverso = 235 ; soma = 532 + 235 = 767).
"""
# Entrada
numero = int(input(f'Digite um número com 3 dígitos: '))

# Processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10
contrario = centena + dezena * 10 + unidade * 100
soma = numero + contrario

# Saída
print(f'A soma entre {numero} e o seu contrário {contrario} é igual a {soma}')
