"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
· o salário antes do reajuste;
· o percentual de aumento aplicado;
· o valor do aumento;
· o novo salário, após o aumento.
"""


def main():
    salario = float(input("Digite o seu salário: "))
    reajuste, percentual, aumento = calc_aumento(salario)
    print(f"""
    Salário sem reajuste: {salario}
    Percentual do reajuste: {percentual}
    Aumento: {aumento}
    Salário com reajuste: {reajuste}
    """)


def calc_aumento(salario):
    if salario <= 280:
        reajuste = salario * 1.2
        percentual = "20%"
        aumento = reajuste - salario
        return reajuste, percentual, aumento
    elif salario <= 700:
        reajuste = salario * 1.15
        percentual = "15%"
        aumento = reajuste - salario
        return reajuste, percentual, aumento
    elif salario <= 1500:
        reajuste = salario * 1.1
        percentual = "10%"
        aumento = reajuste - salario
        return reajuste, percentual, aumento
    else:
        reajuste = salario * 1.05
        percentual = "5%"
        aumento = reajuste - salario
        return reajuste, percentual, aumento


if __name__ == "__main__":
    main()
