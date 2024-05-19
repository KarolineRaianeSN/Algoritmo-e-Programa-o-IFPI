"""
Leia uma data (dia/mês/ano) e verifique se a data é ou não válida
"""

def main():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    validar_data(dia,mes,ano)

def validar_data(dia,mes,ano):
    if mes == 2 and dia > 29:
        return print("Não é uma data válida")
    if dia <= 31 and mes <=12:
        return print("É uma data válida")
    else:
        return print("Não é uma data válida")


if __name__ == "__main__":
    main()