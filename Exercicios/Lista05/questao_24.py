"""A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
escreva:
a) média de salário da população;
b) média de número de filhos;
c) percentual de pessoas com salário de até R$ 1.000,00."""
def main():

    habitantes = int(input("Número de habitantes: "))
    salario_total = 0
    total_filhos = 0
    salario_ate_1000 = 0

    for i in range(habitantes):
        salario = int(input("Salário: "))
        filhos = int(input("Número de filhos: "))

        salario_total += salario
        total_filhos += filhos
        if salario <= 1000:
            salario_ate_1000 += 1

    media_salario = salario_total / habitantes
    media_filhos = total_filhos / habitantes
    perc_salario_1000 = (salario_ate_1000 / habitantes) * 100

    resultado = f"""
    - Média de salário da população: R$ {media_salario:.2f}
    - Média de filhos por habitante: {media_filhos:.2f} filhos
    - Percentual de habitantes que ganha até R$ 1000,00: {perc_salario_1000:.2f} %"""
    print(resultado)

main()