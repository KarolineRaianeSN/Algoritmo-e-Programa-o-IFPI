"""
Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu
nascimento e a data (dia, mês e ano) atual.
"""
def main():
    dia_atual = int(input("Digite o dia atual: "))
    mes_atual = int(input("Digite o mês atual: "))
    ano_atual = int(input("Digite o ano atual: "))
    dia_nascimento = int(input("Digite o dia do seu nascimento: "))
    mes_nascimento = int(input("Digite o mês do seu nascimento: "))
    ano_nascimento = int(input("Digite o ano do seu nascimento: "))

    calculo_idade(dia_atual, dia_nascimento, mes_atual, mes_nascimento, ano_atual, ano_nascimento)


def calculo_idade(dia_atual, dia_nascimento, mes_atual, mes_nascimento, ano_atual, ano_nascimento):
    idade_ano = ano_atual - ano_nascimento
    idade_mes = mes_atual - mes_nascimento
    idade_dia = dia_atual - dia_nascimento

    if mes_atual < mes_nascimento:
        idade_ano -= 1

        if dia_atual < dia_nascimento:
            idade_mes = 12 + idade_mes - 1
            idade_dia = 30 + idade_dia



    else:

        if dia_atual < dia_nascimento:
            idade_mes = idade_mes - 1
            idade_dia = 30 + idade_dia




    return print(f"Você tem {idade_ano} anos, {idade_mes} meses e {idade_dia} dias")


if __name__ == "__main__":
    main()
