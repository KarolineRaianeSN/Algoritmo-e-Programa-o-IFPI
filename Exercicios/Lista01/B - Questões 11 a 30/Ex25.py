'''
Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.
'''

#Entrada
m = int(input(f'Digite um valor em m: '))

#Processamento
km = m // 1000
metros = m % 1000

#Saída
print(f'{m} m equivalem a {km} quilometros e {metros} metros')