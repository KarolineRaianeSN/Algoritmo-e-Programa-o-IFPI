"""
Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro
valor deve aparecer valor inválido.
"""
def main():

    menu()
    dia = int(input("Digite o número correspondente ao dia da semana: "))
    escolha = dia_semana(dia)
    print(escolha)


def menu():
    print("""
    1 - Domingo
    2 - Segunda-feira
    3 - Terça-feira
    4 - Quarta-feira
    5 - Quinta-feira
    6 - Sexta-feira
    7 - Sábado""")


def dia_semana(dia):
    if dia == 1:
        return "Domingo"
    elif dia == 2:
        return "Segunda-feira"
    elif dia == 3:
        return "Terça-feira"
    elif dia == 4:
        return "Quarta-feira"
    elif dia == 5:
        return "Quinta-feira"
    elif dia == 6:
        return "Sexta-feira"
    elif dia == 7:
        return "Sábado"
    else:
        return "Opção inválida"

if __name__ == "__main__":
    main()