def main():

    print("""
    CANAIS:
    - 2
    - 4
    - 5
    - 7
    - 10 """)

    audiencia_total = 0
    audiencia_2 = 0
    audiencia_4 = 0
    audiencia_5 = 0
    audiencia_7 = 0
    audiencia_10 = 0

    canal = int(input("Canal: "))
    pessoas = int(input("Número de pessoas assistindo: "))

    while canal != 0:
        if canal == 2:
            audiencia_2 += pessoas
        elif canal == 4:
            audiencia_4 += pessoas
        elif canal == 5:
            audiencia_5 += pessoas
        elif canal == 7:
            audiencia_7 += pessoas
        elif canal == 10:
            audiencia_10 += pessoas

        canal = int(input("Canal: "))
        if canal == 0:
            print("Pesquisa encerrada")
        else:
            pessoas = int(input("Número de pessoas assistindo: "))

        audiencia_total += pessoas

    porc_canal_2 = audiencia_2 / audiencia_total
    porc_canal_4 = audiencia_4 / audiencia_total
    porc_canal_5 = audiencia_5 / audiencia_total
    porc_canal_7 = audiencia_7 / audiencia_total
    porc_canal_10 = audiencia_10 / audiencia_total


    resultado = f""" 
- Canal 2: {porc_canal_2:.2f} %
- Canal 4: {porc_canal_4:.2f} %
- Canal 5: {porc_canal_5:.2f} %
- Canal 7: {porc_canal_7:.2f} %
- Canal 10: {porc_canal_10:.2f} %"""

    print(resultado)


if __name__ == '__main__':
    main()