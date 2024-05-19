"""Escreva a tabuada dos números de 1 a 10."""
def main():

    numero = int(input("Digite a tabuada que deseja exibir: "))

    for i in range(11):
        resultado = i * numero
        print(f"{i} x {numero} = {resultado}")

main()