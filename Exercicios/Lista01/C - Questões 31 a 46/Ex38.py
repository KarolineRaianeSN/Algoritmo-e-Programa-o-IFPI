"""
Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o
resultado em forma de fração.
"""
# Entrada
numerador_1 = int(input(f'Digite o valor do primeiro numerador: '))
denominador_1 = int(input(f'Digite o valor do primeiro denominador: '))
numerador_2 = int(input(f'Digite o valor do segundo numerador: '))
denominador_2 = int(input(f'Digite o valor do segundo denominador: '))

# Processamento
numerador_resultado_1 = denominador_2 * numerador_1 + denominador_1 * numerador_2
denominador_resultado_1 = denominador_1 * denominador_2

# Saída
print(f'A soma entre {numerador_1}/{denominador_1} e {numerador_2}/{denominador_2} é igual a {numerador_resultado_1}/{denominador_resultado_1}')


