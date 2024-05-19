'''
Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele corresponde.
'''
#Entrada
minutos_entrada = int(input(f'Digite um valor em minutos: '))

#Processamento
dias = minutos_entrada // 1440
horas = (minutos_entrada % 1440) // 60
minutos_saida = minutos_entrada % 60


#Saída
print(f'{minutos_entrada} minutos equivalem a {dias} dias {horas} horas e {minutos_saida} minutos')