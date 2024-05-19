"""
Leia 3 (três) números (cada número corresponde a um lado do triângulo), verifique e escreva se os 3
(três) números formam um triângulo (a soma de dois lados não pode ser menor que o terceiro lado). Se
formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).
"""
def main():
    lado1 = int(input("Digite o primeiro número: "))
    lado2 = int(input("Digite o segundo número: "))
    lado3 = int(input("Digite o terceiro número: "))

    forma_triangulo(lado1,lado2,lado3)

def forma_triangulo(lado1,lado2,lado3):
    if lado1 + lado2 > lado3 or lado2 + lado3 > lado1 or lado1 + lado3 > lado2:
        classifica = classificacao(lado1, lado2, lado3)
        return print (f"Forma um triângulo {classifica}")
    else:
        return print("Não forma um triângulo")
def classificacao():
    if forma_triangulo(lado1,lado2lado3):
        if lado1 == lado2 == lado3:
            return "equilátero"
        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            return "isóceles"
        else:
            return "escaleno"

if __name__ == "__main__":
    main()