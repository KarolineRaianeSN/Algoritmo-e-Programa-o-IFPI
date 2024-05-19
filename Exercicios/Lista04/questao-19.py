def main():

    numero = int(input("Número de identificação: "))
    peso = int(input("Peso: "))

    numero_menor = numero
    peso_menor = peso
    numero_maior = numero
    peso_maior = peso

    while numero != 0:
        if peso < peso_menor:
            peso_menor = peso
            numero_menor = numero
        if peso > peso_maior:
            peso_maior = peso
            numero_maior = numero

        numero = int(input("Número de identificação: "))
        if numero == 0:
            print("Programa encerrado")
        else:
            peso = int(input("Peso: "))

    resultado = f"""
Boi mais gordo:
- Número: {numero_maior} 
- Peso: {peso_maior}
Boi mais magro:
- Número: {numero_menor}
- Peso: {peso_menor}"""

    print(resultado)

main()