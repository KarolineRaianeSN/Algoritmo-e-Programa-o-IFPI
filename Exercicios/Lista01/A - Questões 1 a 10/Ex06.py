'''
Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)
'''
#Entrada
velocidade_km = int(input(f'Digite o valor da velovidade em km/h: '))

#Procesamento
velocidade_ms = velocidade_km * 3.6

#Saída
print(f'O valor da velocidade em m/s é igual a {velocidade_ms} m/s')