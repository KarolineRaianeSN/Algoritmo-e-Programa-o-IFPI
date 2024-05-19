"""
Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.
"""
def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))
    numero4 = int(input("Digite o quarto número: "))
    numero5 = int(input("Digite o quinto número: "))


    comparacao(numero1, numero2, numero3, numero4, numero5)

def media(numero1,numero2,numero3,numero4,numero5):
    return (numero1 + numero2 + numero3 + numero4 + numero5) / 5


def comparacao(numero1, numero2, numero3, numero4, numero5):
    maiores = []
    m = media(numero1, numero2, numero3, numero4, numero5)
    if numero1 > m:
        maiores.append(numero1)
    if numero2 > m:
        maiores.append(numero2)
    if numero3 > m:
        maiores.append(numero3)
    if numero4 > m:
        maiores.append(numero4)
    if numero5 > m:
        maiores.append(numero5)
    print(f"Os números {maiores} são maiores que a média")

if __name__ == "__main__":
    main()
