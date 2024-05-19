"""
Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.
"""
def main():

    lado1 = int(input("Digite o lado 1 do triângulo: "))
    lado2 = int(input("Digite o lado 2 do triângulo: "))
    lado3 = int(input("Digite o lado 3 do triângulo: "))

    calc_hipotenusa(lado1, lado2, lado3)

def calc_hipotenusa(lado1, lado2, lado3):
    if lado1 **2 == lado2 **2 + lado3 **2:
        hipotenusa = lado1
        cateto1 = lado2
        cateto2 = lado3
        print(f"A hipotenusa é igual a {hipotenusa} e osa catetos são iguais a {cateto1} e {cateto2}")
    elif lado2 **2 == lado1 **2 + lado3 **2:
        hipotenusa = lado2
        cateto1 = lado1
        cateto2 = lado3
        print(f"A hipotenusa é igual a {hipotenusa} e osa catetos são iguais a {cateto1} e {cateto2}")

    elif lado3 **2 == lado1 **2 + lado2 **2:
        hipotenusa = lado3
        cateto1 = lado1
        cateto2 = lado3
        print(f"A hipotenusa é igual a {hipotenusa} e osa catetos são iguais a {cateto1} e {cateto2}")
    else:
        print("Não é um triângulo retângulo")

if __name__ == "__main__":
    main()