'''
Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)
'''

#Entrada
numero = int(input(f'Digite um número com 3 casas: '))

#Processamento
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10

#Saída
print(f'O número {numero} ao contrário é igual a {unidade}{dezena}{centena}')
