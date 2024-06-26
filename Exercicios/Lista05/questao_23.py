"""Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
líquido do funcionário."""
def main():

    funcionarios = int(input("Número de funcionários: "))



    for i in range(funcionarios):
        codigo = int(input("Código do funcionário: "))
        horas_trabalhadas = int(input("Horas trabalhadas: "))
        dependentes = int(input("Número de dependentes: "))

        salario = calc_salario(horas_trabalhadas)
        adicional_dependentes = calc_dependentes(dependentes)
        salario_total = salario + adicional_dependentes
        ir, inss = calc_descontos(salario)
        descontos = ir + inss
        salario_liquido = salario - descontos + adicional_dependentes

        print(f"""
        ----- CONTRA-CHEQUE DE FUNCIONÁRIO {codigo} -----
        - Salário: R$ {salario_total}
        - IR: R$ {ir}
        - INSS: R$ {inss}
        - Descontos: R$ {descontos}
        - Salário líquido: R$ {salario_liquido}
        -------------------------------------------------""")

def calc_salario(horas_trabalhadas):
    salario = horas_trabalhadas * 12

    return salario


def calc_descontos(salario):
    ir = salario * 8.5/100
    inss = salario * 5/100

    return ir, inss

def calc_dependentes(dependentes):
    adicional_dependentes = dependentes * 40

    return adicional_dependentes

main()