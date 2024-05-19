"""
Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
contrario, é arredondado para o inteiro imediatamente inferior.
"""
def main():

    numero = float(input("Digite o número: "))
    arredondamento(numero)
def arredondamento(numero):
    if numero - round(numero) >= 0.5:
        arredondamento_maior = round(numero + 0.5)
        return print(arredondamento_maior)
    else:
        arredondamento_menor = round(numero - 0.5)
        return print(arredondamento_menor)
if __name__ == "__main__":
    main()