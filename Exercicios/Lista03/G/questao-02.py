"""
Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.
"""

def main():

    menu()
    opcao = input("Digite F para feminino e M para masculino: ")
    escolha(opcao)

def escolha(opcao):
    if opcao == "F":
        return print("Feminino")
    elif opcao == "M":
        return print("Masculino")
    else:
        return print("Opção inválida")

def menu():
    print("""
    F - Feminino
    M - Masculino""")

if __name__ == "__main__":
    main()