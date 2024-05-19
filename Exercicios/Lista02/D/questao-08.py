"""
Leia data atual (dia, mês, ano) e data de nascimento (dia, mês, ano). Calcule e escreva sua idade exata. (em anos)
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
    if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
        idade_ano -= 1

    return print(f"Você tem {idade_ano} anos")


if __name__ == "__main__":
    main()
