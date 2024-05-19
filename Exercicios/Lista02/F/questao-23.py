"""
Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.
"""


def main():
    dia1 = int(input("Digite o dia da primeira data: "))
    mes1 = int(input("Digite o mes da primeira data: "))
    ano1 = int(input("Digite o ano da primeira data: "))
    dia2 = int(input("Digite o dia da segunda data: "))
    mes2 = int(input("Digite o mes da segunda data: "))
    ano2 = int(input("Digite o ano da segunda data: "))

    comparacao(dia1, mes1, ano1, dia2, mes2, ano2)


def comparacao(dia1, mes1, ano1, dia2, mes2, ano2):
    if ano1 == ano2:
        if mes1 == mes2:
            if dia1 == dia2:
                return print("Data 1 é igual a data 2")
            elif dia1 > dia2:
                return print("Data 1 é mais recente que a data 2")
            else:
                return print("Data 2 é mais recente que a data 1")
        elif mes1 > mes2:
            return print("Data 1 é mais recente que a data 2")
        else:
            return print("Data 2 é mais recente que a data 1")
    elif ano1 > ano2:
        return print("Data 1 é mais recente que a data 2")
    else:
        return print("Data 2 é mais recente que a data 1")


if __name__ == "__main__":
    main()
