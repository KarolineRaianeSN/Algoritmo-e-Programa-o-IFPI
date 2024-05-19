"""
Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele
fuma, o no de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros).
"""

# Entrada
tempo = int(input(f'Quantidade de anos que a pessoa fuma: '))
cigarros = int(input(f'Quantidade de cigarros fumados por dia: '))
valor_carteira = int(input(f'Valor de uma carteira de cigarro: '))

# Processamento
tempo_em_dias = tempo * 360
valor_total = ((cigarros / 20) * valor_carteira) * tempo_em_dias

# Saída
print(f'O valor total gasto com {cigarros} cigarros por dia é igual a {valor_total} reais')