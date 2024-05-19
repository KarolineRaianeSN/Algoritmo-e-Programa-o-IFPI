def main():

    duracao = float(input("Qual a duração do curso? "))
    mensalidade = int(input("Qual o valor da mensalidade? "))
    selic = float(input("Qual a a taxa SELIC? "))
    salario = float(input("Qual o salário mínimo vigente? "))
    renda_familiar = float(input("Qual a renda familiar? "))
    pessoas_familia = int(input("Quantas pessoas há na família? "))
    ano_início = int(input("Ano de início no curso: "))
    semestre_inicio = int(input("Qual o semestre de início no curso? "))



    situacao = calc_situacao(renda_familiar, salario)
    renda = renda_percapita(renda_familiar, pessoas_familia)
    selic = calc_selic(renda, salario, selic)
    duracao_curso = calc_duracao_curso(duracao)
    juros = calc_juros(mensalidade, selic, duracao_curso)
    valor_financiado = calc_valor_financiado(mensalidade, duracao_curso)
    taxa_fixa = calc_taxa_fixa(duracao_curso)
    carencia = calc_carencia()
    parcela, num_parcelas = calc_parcela(juros,taxa_fixa,carencia)
    saldo_devedor = calc_saldo_devedor(valor_financiado, juros, taxa_fixa, carencia)
    final =  calc_final(taxa_fixa, carencia,  juros, valor_financiado)
    renda_pos = pos_carencia(parcela, final)
    inicio_pagamento, final_pagamento = calc_duracao_pagamento(ano_inicio, semestre_inicio, duracao, num_parcelas)


    print(f"""
    O financiamento foi de R$: {situacao}
    Valor a ser finaniciado R$: {valor_financiado}
    Valor total de júros R$: {juros}
    Valor pago durante o curso R$: {taxa_fixa + mensalidade}
    Parcela do financiamento R$: {parcela}
    Renda mínima pós-carência R$: {renda_pos}
    Ano início pagamento: {inicio_pagamento}
    Ano final do pagamento: {final_pagamento} """)


def renda_percapita(renda_familiar, pessoas_familia):
    return renda_familiar / pessoas_familia


def calc_situacao(renda, salario):
    if renda <= 3 * salario:
        return "Aprovado"
    else:
        return "Não aprovado"



def calc_selic(renda, salario, selic):
    if renda <= 1.5 * salario:
        return 0.1 * selic
    elif renda <= 2 * salario:
        return 0.15 * selic
    elif renda <= 2.5 * salario:
        return 0.2 * selic
    else:
        return 0.25 * selic


def calc_duracao_curso(duracao):
    return duracao * 12


def calc_juros(mensalidade, selic, duracao_curso):
    return (mensalidade * selic) * duracao_curso


def calc_valor_financiado(mensalidade, duracao_curso):
    return mensalidade * duracao_curso


def valor_total(valor_financiado, juros, taxa_fixa, carencia):
    return valor_financiado + juros + taxa_fixa + carencia


def calc_taxa_fixa(duracao_curso):
    return (duracao_curso / 3) * 150


def calc_carencia():
    return 150 * 18


def calc_saldo_devedor(valor_financiado, juros, taxa_fixa, carencia):
    return juros + valor_financiado - taxa_fixa - carencia


def calc_parcela(saldo_devedor,duracao_curso):
    num_parcelas = 4 * duracao_curso
    valor_parcela = saldo_devedor / num_parcelas
    return valor_parcela, num_parcelas


def calc_duracao_pagamento(ano_inicio, semestre_inicio, duracao, num_parcelas):
    inicio = ano_inicio + duracao
    if semestre_inicio == 1:
        inicio += 2
    else:
        inicio += 2
    final = ano_inicio + duracao + (num_parcelas // 12)
    return inicio,final


def pos_carencia(parcela, final):


def calc_final(taxa_fixa, carencia,  juros, valor_financiado):
    final = taxa_fixa + carencia + juros + valor_financiado


main()