'''
Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).
'''

#Entrada
numero = int(input(f'Digite uma centena: '))

#Processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

total = centena + dezena + unidade

#Saída
print(f'O valor de {centena} + {dezena} + {unidade} = {total} ')