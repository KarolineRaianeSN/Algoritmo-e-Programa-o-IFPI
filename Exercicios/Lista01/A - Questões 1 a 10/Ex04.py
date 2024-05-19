'''
Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).
'''

#Entradas
dolar = int(input(f'Cotação do dólar atual: '))
reais = int(input(f'Valor em  dólares: '))

#Processamento
valor = dolar * reais

#Saída
print(f'O valor de ${reais} em reais é igual a R${valor}')