"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
Até 5 Kg               |  Acima de 5 Kg
File R$ 4,90 por Kg    | R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg | R$ 6,80 por Kg
Picanha R$ 6,90 por Kg | R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o
cliente receberá ainda um desconto de 5% sobre o total a compra. Escreva um programa que peça o tipo
e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""


def main():
    menu()
    tipo = input("Digite o tipo de carne que deseja comprar: ")
    peso = int(input("Digite a quantidade (em Kg) de carne que deseja comprar: "))
    cartao = input("Irá usar o cartão Tabajara?[Sim/Nao] ")

    valor_total = calc_compra(tipo, peso)
    valor_com_desconto, desconto, tipo_compra = operacao_cartao(valor_total, cartao)

    print(f"""
    Tipo de carne: {tipo}
    Quantidade de carne: {peso}
    Preço total: {valor_total:.2f}
    Tipo de pagamento: {tipo_compra}
    Desconto: {desconto:.2f}
    Valor a pagar: {valor_com_desconto:.2f}
    """)


def menu():
    print("""
    Até 5 Kg           |  Acima de 5 Kg
File R$ 4,90 por Kg    | R$ 5,80 por Kg
Alcatra R$ 5,90 por Kg | R$ 6,80 por Kg
Picanha R$ 6,90 por Kg | R$ 7,80 por Kg""")


def calc_compra(tipo, peso):
    if tipo == "Filé":
        return calc_file(peso)
    elif tipo == "Alcatra":
        return calc_alcatra(peso)
    elif tipo == "Picanha":
        return calc_picanha(peso)
    return 0


def calc_file(peso):
    return peso * (4.90 if peso <= 5 else 5.80)


def calc_alcatra(peso):
    return peso * (5.90 if peso <= 5 else 6.80)


def calc_picanha(peso):
    return peso * (6.90 if peso <= 5 else 7.80)


def operacao_cartao(valor_total, cartao):
    if cartao == "Sim":
        valor_com_desconto = valor_total * 0.95
        desconto = valor_total * 0.05
        tipo_compra = "Cartão Tabajara"
    else:
        valor_com_desconto = valor_total
        desconto = 0
        tipo_compra = "Convencional"
    return valor_com_desconto, desconto, tipo_compra


if __name__ == "__main__":
    main()
