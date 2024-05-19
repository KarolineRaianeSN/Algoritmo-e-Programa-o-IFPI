def main():

    salario = 0
    soma_salarios = 0
    soma_salarios_ajuste = 0

    salario = int(input("Digite o salário do funcionário: "))

    while salario != 0:

        soma_salarios += salario
        ajuste = calc_ajuste(salario)
        novo_salario = salario + ajuste
        soma_salarios_ajuste += salario + ajuste
        print(f"Novo salário: {novo_salario}")

        salario = int(input("Digite o salário do funcionário: "))

    diferenca = soma_salarios_ajuste - soma_salarios

    resultado = f"""
    Soma dos salários atuais: {soma_salarios}
    Soma dos salários reajustados: {soma_salarios_ajuste}
    Diferença entre a soma de salários atuais e reajustados: {diferenca} """

    print(resultado)


def calc_ajuste(salario):
    if salario < 3000:
        ajuste = salario * 0.25
    elif salario < 6000:
        ajuste = salario * 0.20
    elif salario < 1000:
        ajuste = salario * 0.15
    else:
        ajuste = salario * 0.10
    return ajuste

if __name__ == '__main__':
    main()