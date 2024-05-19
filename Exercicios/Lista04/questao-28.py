import random
def main():
    numero = random.randint(1, 1000)

    palpite = int(input("Digite um número: "))

    procurando_numero = True


    tentativas = 1

    while procurando_numero == True:

        if palpite < numero:
            print("Menor")
        elif palpite > numero:
            print("Maior")


        if palpite == numero:
            print(f"Acertou com {tentativas} tentativas")
            procurando_numero = False
        else:
            palpite = int(input("Digite um número: "))
        tentativas += 1

if __name__ == '__main__':
    main()