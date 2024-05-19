"""
Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
(IMC = peso / altura2

). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso

(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).
"""

def main():
    altura = float(input("Digite uma altura em metros: "))
    peso = int(input("Digite um peso em kg: "))

    print(f"De acordo com sua altura e peso você está classificado como "
          f"{imc_classificacao(altura,peso)}")


def imc_classificacao(altura,peso):
    imc = peso / altura ** 2
    if imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Obeso"
    else:
        return "Obesidade mórbida"
if __name__ == "__main__":
    main()