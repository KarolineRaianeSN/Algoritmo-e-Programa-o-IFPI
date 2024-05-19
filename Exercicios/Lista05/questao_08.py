"""Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos."""
def main():

    numero = int(input("Digite um número: "))
    limite_inferior = int(input("Digite o limite inferior: "))
    limite_superior = int(input("Digite o limite superior: "))

    for i in range(limite_inferior,limite_superior):
        if i % numero == 0:
            print(i)



main()