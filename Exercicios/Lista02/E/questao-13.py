"""
Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são
diferentes.
"""
def main():
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))
    numero4 = int(input("Digite o quarto número: "))
    numero5 = int(input("Digite o quinto número: "))

    comparacao(numero1, numero2, numero3, numero4, numero5)

def comparacao(numero1, numero2, numero3, numero4, numero5):
    maior = max(numero1, numero2, numero3, numero4, numero5)
    menor = min(numero1, numero2, numero3, numero4, numero5)
    return print(f"O número maior é igual a {maior} e o número menor é igual a {menor}")

if __name__ == "__main__":
    main()