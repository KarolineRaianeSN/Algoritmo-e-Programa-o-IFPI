def main():
    peca_1 = input()
    peca_2 = input()

    peca_1_valores = peca_1.split(" ")
    peca_2_valores = peca_2.split(" ")
    peca1_codigo = peca_1_valores[0]
    peca1_numero = float(peca_1_valores[1])
    peca1_valor = float(peca_1_valores[2])
    peca2_codigo = peca_2_valores[0]
    peca2_numero = float(peca_2_valores[1])
    peca2_valor = float(peca_2_valores[2])


    valor_total1 = peca1_numero * peca1_valor
    valor_total2 = peca2_numero * peca2_valor
    valor_total = valor_total1 + valor_total2

    print(f'VALOR A PAGAR: R$ {valor_total:.2f}')

main()