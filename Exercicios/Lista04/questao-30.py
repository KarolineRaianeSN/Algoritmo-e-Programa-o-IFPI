def main():

    produto = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))
    quantidade = int(input("Quantidade do produto: "))

    total = preco * quantidade

    if quantidade < 10 and quantidade <= 20:
        desconto = total * 0.1
    elif quantidade <= 50:
        desconto = total * 0.2
    elif quantidade < 50:
        desconto = total * 0.25

    total = total - desconto

    print(f"{produto} - R$ {total:.2f}")

if __name__ == '__main__':
    main()