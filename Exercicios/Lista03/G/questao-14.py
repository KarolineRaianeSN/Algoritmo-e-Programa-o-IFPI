"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
1. Álcool:
· até 20 litros, desconto de 3% por litro
· acima de 20 litros, desconto de 5% por litro
2. Gasolina:
· até 20 litros, desconto de 4% por litro
· acima de 20 litros, desconto de 6% por litro.
Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""


def main():
    menu()
    tipo = int(input("Digite o tipo de combustível: "))
    litros = int(input("Digite a quantidade de litros que deseja abastecer: "))

    valor = escolha_combustivel(tipo, litros)
    print(f"O valor a ser pago será de: R$ {valor}")


def menu():
    print("""
    1- Álcool
    2- Gasolina""")


def escolha_combustivel(tipo, litros):
    if tipo == 1:
       return desconto_alcool(tipo, litros)
    if tipo == 2:
        return desconto_gasolina(tipo, litros)


def desconto_gasolina(tipo, litros):
    if litros < 20:
        valor = litros * 2.50
        desconto = valor * 0.03
        valor_total = valor - desconto
    else:
        valor = litros * 2.50
        desconto = valor * 0.05
        valor_total = valor - desconto
    return valor_total


def desconto_alcool(tipo, litros):
    if litros < 20:
        valor = litros * 1.90
        desconto = valor * 0.04
        valor_total = valor - desconto
    else:
        valor = litros * 1.90
        desconto = valor * 0.06
        valor_total = valor - desconto
    return valor_total


if __name__ == "__main__":
    main()
