'''
Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.
'''

#Entrada
nota1 = int(input(f'Digite a primeira nota: '))
peso1 = int(input(f'Digite o peso da primeira nota: '))
nota2 = int(input(f'Digite a segunda nota: '))
peso2 = int(input(f'Digite o peso da segunda nota: '))
nota3 = int(input(f'Digite a terceira nota: '))
peso3 = int(input(f'Digite o peso da terceira nota: '))

#Processamento
media = (nota1*peso2 + nota2*peso2 + nota3*peso3) / (peso1+peso2+peso3)

#Saída
print(f'A média das notas é igual a {media}')