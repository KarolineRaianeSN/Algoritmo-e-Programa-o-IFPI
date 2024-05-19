'''
Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.
'''
#Entrada
numero1 = int(input(f'Digite o primeiro número: '))
numero2 = int(input(f'Digite o segundo número: '))
numero3 = int(input(f'Digite o terceiro número: '))

#Processamento
soma = numero1 + numero2
diferenca = numero2 - numero3

#Saída
print(f'A soma dos dois primeiros números é igual a {soma} e a diferença entre os dos últimos números e igual a {diferenca}')