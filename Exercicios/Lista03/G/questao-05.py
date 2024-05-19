"""
Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é
sempre pelo mais barato.
"""
def main():

    produto_a = float(input("Digite o valor do produto A: "))
    produto_b = float(input("Digite o valor do produto B: "))
    produto_c = float(input("Digite o valor do produto C: "))

    produto_escolhido = escolha(produto_a, produto_b, produto_c)
    print(f"O produto que deve ser comprado deverá ser o {produto_escolhido}")

def escolha(produto_a, produto_b, produto_c):
    if produto_a < produto_b and produto_a < produto_c:
        return "produto A"
    elif produto_b < produto_a and produto_b < produto_c:
        return "produto B"
    else:
        return "produto C"
if __name__ == "__main__":
    main()