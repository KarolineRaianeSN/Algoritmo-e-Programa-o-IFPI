"""
Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação
sobre os dois valores lidos.
"""
def main():
    menu()
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    escolha = int(input("Digite a operação que deseja realizar: "))

    opcao(numero1,numero2,escolha)


def opcao(numero1,numero2,escolha):
    if escolha == 1:
        soma = numero1 + numero2
        print(f"A soma dos números é igual a {soma}")
    elif escolha == 2:
        subtracao = numero1 - numero2
        print(f"A subtração dos números é igual a {subtracao}")
    elif escolha == 3:
        multiplicacao = numero1 * numero2
        print(f"A multiplicação dos números é igual a {multiplicacao}")
    elif escolha == 4:
        divisao = numero1 / numero2
        print(f"A divisão dos números é igual a {divisao}")
    else:
        print("Opção inválida")


def menu():
    print('''-------------------------------
          Opção 1: Adição
          Opção 2: Subtração
          Opção 3: Multiplicação
          Opção 4: Divisão
          -------------------------------''')
if __name__ == "__main__":
    main()