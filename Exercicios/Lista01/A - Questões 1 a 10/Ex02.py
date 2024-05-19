'''
Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.
'''
#Entrada

horas = int(input(f'Valor em horas: '))
minutos = int(input(f'Valor em minutos: '))

#Processamento
valor_final = horas * 60 + minutos

#Saída
print(f'O valor final em minutos é igual a: {valor_final}')



