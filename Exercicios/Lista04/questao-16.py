def main():
    saldo_emprestimo = 3000
    pagamento_diario = 200
    taxa_juros = 0.85

    dias = calcular_dias_emprestimo(saldo_emprestimo, pagamento_diario, taxa_juros)

    print("São necessários", dias, "dias úteis para concluir o pagamento do empréstimo.")
def calcular_dias_emprestimo(saldo_emprestimo, pagamento_diario, taxa_juros):
    dias = 0
    while saldo_emprestimo > 0:
        saldo_emprestimo += saldo_emprestimo * taxa_juros / 100
        saldo_emprestimo -= pagamento_diario
        if saldo_emprestimo < 0:
            saldo_emprestimo = 0
        dias += 1  #
    return dias

if __name__ == '__main__':
    main()