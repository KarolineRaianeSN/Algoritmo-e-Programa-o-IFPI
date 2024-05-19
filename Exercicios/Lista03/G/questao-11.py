"""
Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades
"""
def main():

    numero = int(input("Digite um número menor do que 1000: "))
    centena, dezena, unidade = calc_digitos(numero)
    print(f"O número possui {centena} centenas, {dezena} dezenas e {unidade} unidades")


def calc_digitos(numero):
    centena = numero // 100
    resto = numero % 100
    dezena = resto // 10
    unidade = resto % 10
    return centena, dezena, unidade

if __name__ == "__main__":
    main()