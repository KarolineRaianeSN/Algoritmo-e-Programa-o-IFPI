"""
Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.
"""
# Entrada
print(f'Digite a sua idade exatamente em anos, meses e dias')
idade_anos = int(input(f'Digite a sua idade em anos: '))
idade_meses = int(input(f'{idade_anos} anos e quantos meses? '))
idade_dias = int(input(f'{idade_anos} anos, {idade_meses} meses e quantos dias? '))

# Processamento
dias_totais = idade_anos * 360 + idade_meses * 12 + idade_dias

# Saída
print(f'A sua idade em dias é igual a {dias_totais}')