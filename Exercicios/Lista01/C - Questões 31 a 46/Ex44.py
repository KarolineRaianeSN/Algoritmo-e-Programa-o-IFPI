"""
Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada pelo usuário.
"""
# Entrada
latao = int(input(f'Digite a quantidade de latão que deseja obter: '))

# Processamento
cobre = latao * 0.7
zinco = latao * 0.3

# Saída
print(f'Para obtermos uma quantidade de {latao} kg de latão serão necessários {cobre} kg de cobre e {zinco} kg de zinco')