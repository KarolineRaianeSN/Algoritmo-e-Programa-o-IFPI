'''
Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).
'''

#Entrada
temperatura_f = int(input(f'Digite o valor da temperatura em ºF: '))

#Processamento
temperatura_celcius = (temperatura_f * 5 - 160) / 9

#Saída
print(f'O valor de {temperatura_f} ºF em Celsius é igual a {temperatura_celcius} ºC')