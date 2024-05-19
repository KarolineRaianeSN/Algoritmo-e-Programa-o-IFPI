'''
Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.
'''

#Entrada
d = int(input(f'Digite um número de dias: '))

#Processamento
semanas = d // 7
dias = d % 7

#Saída
print(f'{d} dias equivalem a {semanas} semanas e {dias} dias')