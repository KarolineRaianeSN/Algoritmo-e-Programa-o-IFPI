'''
Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele corresponde.
'''
#Entrada
horas_entrada = int(input(f'Digite um valor em horas: '))

#Processamento
semanas = horas_entrada // 168
dias = (horas_entrada % 168) // 24
horas_saida = horas_entrada % 24


#Saída
print(f'{horas_entrada} horas equivalem a {semanas} semanas {dias} dias e {horas_saida} horas')