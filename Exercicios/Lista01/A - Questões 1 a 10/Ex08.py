'''
Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.
'''

#Entrada
numero1 = int(input(f'Digite o primeiro número: '))
numero2 = int(input(f'Digite o segundo número: '))

#Processamento
soma = numero1 + numero2
subtracao = numero1 - numero2
divisao = soma / subtracao

#Saída
print(f'O valor total da divisão entre a soma e a subtração de {numero1} e {numero2} é igual a: {divisao}')