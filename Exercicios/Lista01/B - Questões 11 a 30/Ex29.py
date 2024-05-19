'''
Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.
'''
#Entrada
meses_entrada = int(input(f'Digite um valor em meses: '))

#Processamento
anos = meses_entrada // 12
meses_saida = meses_entrada % 12

#Saída
print(f'{meses_entrada} meses equivalem a {anos} anos e {meses_saida} meses')