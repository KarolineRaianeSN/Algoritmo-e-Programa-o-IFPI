"""
Leia quatro números (opção,num1,num2 e num3) e que escreva o valor de num1 se a opção igual a 1, o valor de num2 se
opção for igual a 2 e o
valor de num3 se a opção for igual a 3
"""

def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    opcao = int(input("Digite a opção que deseja exibir: "))

    escolha(opcao,num1,num2,num3)

def escolha(opcao, num1, num2, num3):
    if opcao == 1:
        return num1
    elif opcao == 2:
        return num2
    elif opcao == 3:
        return num3
    else:
        return "Opção inválida"
if __name__ == "__main__":
    main()