"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Até 5 Kg | Acima de 5 Kg
Morango R$ 2,50 por Kg | R$ 2,20 por Kg
Maçã R$ 1,80 por Kg | R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""


def main():
    menu()
    morango = int(input("Digite a quantidade em Kg de morango que deseja comprar: "))
    maca = int(input("Digite a quantidade em Kg de maçã que deseja comprar: "))

    valor = calc_compra(morango, maca)
    print(f"O valor a ser pago será de {valor:.2f}")


def menu():
    print("""
    Até 5 Kg           | Acima de 5 Kg
Morango R$ 2,50 por Kg | R$ 2,20 por Kg
Maçã R$ 1,80 por Kg    | R$ 1,50 por Kg""")


def calc_compra(morango, maca):
    total_morango = valor_morango(morango)
    total_maca = valor_maca(maca)

    valor_total = total_maca + total_morango

    if morango + maca > 8 or valor_total > 25:
        return valor_total * 0.9
    else:
        return valor_total


def valor_morango(morango):
    if morango > 5:
        preco_morango = morango * 2.20
    else:
        preco_morango = morango * 2.50
    return preco_morango


def valor_maca(maca):
    if maca > 5:
        preco_maca = maca * 1.50
    else:
        preco_maca = maca * 1.80
    return preco_maca


if __name__ == "__main__":
    main()
