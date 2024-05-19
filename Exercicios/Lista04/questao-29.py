def main():

    investimento_mensal = int(input("Investimento mensal: "))
    juros = float(input("Júros: "))

    juros = juros / 100

    decisao = "S"

    juros = 0
    total = 0
    while decisao != "N":
        montante = investimento_mensal * (1 + juros) ** (12)

        juros += montante
        total = (12 * investimento_mensal) + juros

        decisao = input("Deseja processar mais um ano (S/N) ?")


    print(f"R$ {total:.2f} ")

if __name__ == '__main__':
    main()