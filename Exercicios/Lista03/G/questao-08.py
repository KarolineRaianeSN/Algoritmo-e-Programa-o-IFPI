"""
Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00
"""
def main():

    valor_hora = float(input("Digite o valor da hora trabalhada: "))
    quantidade_hora = float(input("Digite o número de horas trabalhada: "))

    salario_liquido, salario_bruto, sindicato, fgts, imposto_renda, total_descontos = calc_salario_liquido(
        valor_hora, quantidade_hora)

    print(f"""
    Salário bruto: R$ {salario_bruto}
    (-) IR(5%): R$ {imposto_renda}
    (-) Sindicato (3%): R$ {sindicato}
    FGTS(11%): R$ {fgts}
    Total de descontos: R$ {total_descontos}
    Salário líquido: R$ {salario_liquido} """)
def calc_salario_bruto(valor_hora,quantidade_hora):
    salario_bruto = valor_hora * quantidade_hora
    return salario_bruto


def calc_imposto_renda(valor_hora, quantidade_hora):
    salario_bruto = calc_salario_bruto(valor_hora, quantidade_hora)
    if salario_bruto <= 900:
        imposto = 0
    elif salario_bruto <= 1500:
        imposto = salario_bruto * 0.05
    elif salario_bruto <= 2500:
        imposto = salario_bruto * 0.1
    else:
        imposto = salario_bruto * 0.2
    return imposto


def calc_sindicato(valor_hora, quantidade_hora):
    salario_bruto = calc_salario_bruto(valor_hora, quantidade_hora)
    taxa_sindicato = salario_bruto * 0.03
    return taxa_sindicato

def calc_fgts(valor_hora, quantidade_hora):
    salario_bruto = calc_salario_bruto(valor_hora, quantidade_hora)
    fgts = salario_bruto * 0.11
    return fgts

def calc_salario_liquido(valor_hora, quantidade_hora):
    salario_bruto = calc_salario_bruto(valor_hora, quantidade_hora)
    sindicato = calc_sindicato(valor_hora, quantidade_hora)
    fgts = calc_fgts(valor_hora, quantidade_hora)
    imposto_renda = calc_imposto_renda(valor_hora, quantidade_hora)
    total_descontos = sindicato + imposto_renda
    salario_liquido = salario_bruto - total_descontos
    return salario_liquido, salario_bruto, sindicato, fgts, imposto_renda, total_descontos

if __name__ == "__main__":
    main()