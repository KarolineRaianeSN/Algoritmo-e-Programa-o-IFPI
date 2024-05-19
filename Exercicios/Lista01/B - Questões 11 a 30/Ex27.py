'''
Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos segundos ele corresponde.
'''

#Entrada
segundos_entrada = int(input(f'Digite um valor em segundos: '))

#Processamento
horas = segundos_entrada // 3600
minutos = (segundos_entrada % 3600) // 60
segundos_saida = segundos_entrada % 60

#Saída
print(f'{segundos_entrada} segundos equivalem a {horas} horas {minutos} minutos e {segundos_saida} segundos')