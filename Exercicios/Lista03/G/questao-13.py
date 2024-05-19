"""
Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima ?"
b) "Esteve no local do crime ?"
c) "Mora perto da vítima ?"
d) "Devia para a vítima ?"
e) "Já trabalhou com a vítima ?"
O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""


def main():
    telefonema = input("Telefonou para a vítima? ")
    local = input("Esteve no local do crime? ")
    moradia = input("Mora perto da vítima? ")
    divida = input("Devia para a vítima? ")
    trabalho = input("Já trabalhou para a vítima? ")

    classificacao = suspeita(telefonema, local, moradia, divida, trabalho)
    print(f"A pessoa será classificada como {classificacao}")


def questionario(telefonema,local, moradia, divida, trabalho):
    sinais = 0
    if telefonema == "Sim" or telefonema == "sim":
        sinais += 1
    if local == "Sim" or local == "sim":
        sinais += 1
    if moradia == "Sim" or moradia == "sim":
        sinais += 1
    if divida == "Sim" or divida == "sim":
        sinais += 1
    if trabalho == "Sim" or trabalho == "sim":
        sinais += 1
    return sinais

def suspeita(telefonema,local,moradia, divida, trabalho):
    sinais = questionario(telefonema,local, moradia, divida, trabalho)
    if sinais <=2:
        return "suspeita"
    elif sinais <= 4:
        return "cúmplice"
    else:
        return "assassino"

if __name__ == "__main__":
    main()