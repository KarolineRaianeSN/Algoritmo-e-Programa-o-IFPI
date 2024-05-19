"""
 Leia uma lista de números e que para cada número lido, escreva o próprio número e a relação de seus
divisores. (flag número = 0).
"""
def main():
    numero = int(input("Digite um número: "))

    while numero != 0:
        calc_divisores(numero)

        numero = int(input("Digite um número: "))

    print("Fim")

def calc_divisores(numero):

    print(f"Divisores de: {numero}")
    candidato = numero
    contador = 0
    divisores = ""
    while candidato > 0:
        if divisor(numero, candidato):
            contador += 1

            divisores += f" {candidato}"
        candidato -= 1
    print(divisores)
    print(f"Total de divisores: {contador}")


def divisor(numero, candidato):
    return numero % candidato == 0

main()