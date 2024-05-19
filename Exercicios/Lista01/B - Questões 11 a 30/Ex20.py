'''
Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)
'''

#Entrada
temperatura_celcius = int(input(f'Digite o valor da temperatura em ºC: '))

#Processamento
temperatura_f = (temperatura_celcius * 9 + 160) / 5

#Saída
print(f'O valor de {temperatura_celcius} ºC em Farenheit é igual a {temperatura_f} ºF')