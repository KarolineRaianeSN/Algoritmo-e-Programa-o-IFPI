def main():

    idade = int(input("Idade: "))
    opiniao = int(input("Quala a sua opinião sobre o filme? (1=ótimo, 2=bom, 3=regular, 4=péssimo) "))

    otimo = 0
    idade_otimo = 0
    regular = 0
    bom = 0
    total = 0

    while idade != -1:
        if opiniao == 1:
            otimo += 1
            idade_otimo += idade
        elif opiniao == 2:
            bom += 1
        elif opiniao == 3:
            regular += 1

        total += 1

        idade = int(input("Idade: "))
        if idade == -1:
            print("Pesquisa encerrada")
        else:
            opiniao = int(input("Quala a sua opinião sobre o filme? (1=ótimo, 2=bom, 3=regular, 4=péssimo) "))


    media_otimo = idade_otimo / otimo
    perc_bom = bom / total

    resultado = f""" 
- Média das idades das pessoas que responderam ótimo: {media_otimo:.2f}
- Quantidade de pessoas que respondeu regular: {regular:.2f}
- Percentual de pessoas que respondeu bom entre os entrevistados: {perc_bom:.2f}"""

    print(resultado)
main()