"""
Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.
"""
# Entrada
idade_dias = int(input(f'Digite a sua idade em dias: '))

# Processamento
anos = idade_dias // 360
meses = (idade_dias % 360) // 12
dias = idade_dias % 30


# Saída
print(f'A sua idade é {anos} anos, {meses} meses e {dias} dias')
