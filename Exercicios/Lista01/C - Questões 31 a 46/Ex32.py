"""
Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.
"""
# Entrada
numero = int(input(f'Digite um número com 3 dígitos: '))

# Processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10
contrario = centena + dezena * 10 + unidade * 100
diferenca = numero - contrario

# Saída
print(f'A diferença entre {numero} e o seu contrário {contrario} é igual a {diferenca}')
