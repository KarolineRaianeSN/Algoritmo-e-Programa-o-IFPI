"""Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
escreva o quadrado dos números lidos."""

def main():
    numero1 = int(input("Digite o primeiro valor: "))
    numero2 = int(input("Digite o segundo valor: "))

    opcao(numero1,numero2)

def calculo(numero1,numero2):
    resto = numero1 % numero2
    return resto


def opcao(numero1,numero2):
    resto = calculo(numero1,numero2)
    if resto == 1:
        soma1 = numero1 + numero2 + resto
        print(f"A soma dos números digitados mais o resto da divisão é igual a {soma1}")
    elif resto == 2:
        impar_ou_par1 = "par" if numero1 % 2 == 0 else "ímpar"
        impar_ou_par2 = "par" if numero2 % 2 == 0 else "ímpar"
        print(f"O número 1 é {impar_ou_par1} e o número 2 é {impar_ou_par2}")
    elif resto == 3:
        soma2 = (numero1 + numero2) * numero1
        print(f"A multiplicação da soma dos números digitados pelo primeiro número é igual a {soma2}")
    elif resto == 4:
        soma3 = (numero1 + numero2) / numero2
        print(f"A divisão da soma dos números digitados pelo segundo número é igual a {soma3}")

    else:
        quadrado1 = numero1**2
        quadrado2 = numero2**2
        print(f"O quadrado de {numero1} é igual a {quadrado1} e o quadrado de {numero2} é igual a {quadrado2}")


if __name__ == "__main__":
    main()