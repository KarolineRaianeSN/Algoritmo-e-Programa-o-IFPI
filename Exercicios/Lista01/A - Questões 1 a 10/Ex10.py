'''
Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.
'''

#Entrada
numero1 = int(input(f'Digite o primeiro número: '))
numero2 = int(input(f'Digite o segundo número: '))

#Processamento
quociente = numero1 / numero2
resto = numero1 % numero2

#Saída
print(f'A divisão de {numero1} por {numero2} é igual a {quociente} com resto igual a {resto}')