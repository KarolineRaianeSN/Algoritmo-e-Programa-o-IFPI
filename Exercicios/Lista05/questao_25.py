"""Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
· 1, 2, 3 = voto para os respectivos candidatos;
· 9 = voto nulo;
· 0 = voto em branco;
Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
a) total de votos para cada candidato;
b) total de votos nulos;
c) total de votos em branco;
d) quem venceu a eleição."""
def main():

    eleitores = int(input("Número de eleitores: "))

    votos_1 = 0
    votos_2 = 0
    votos_3 = 0
    votos_nulo = 0
    vencedor = ""

    for i in range(eleitores):
        voto = int(input("Voto: "))
        if voto == 1:
            votos_1 += 1
        if voto == 2:
            votos_2 += 1
        if voto == 3:
            votos_3 += 1
        if voto == 0:
            votos_nulo += 1

    if votos_1 > votos_2 and votos_1 > votos_3:
        vencedor = "Candidato 1"
    if votos_2 > votos_1 and votos_2 > votos_3:
        vencedor = "Candidato 2"
    if votos_3 > votos_1 and votos_3 > votos_2:
        vencedor = "Candidato 3"
    if votos_1 == votos_2 or votos_1 == votos_3 or votos_2 == votos_3:
        vencedor = "Segundo turno"


    resultado = f"""
    CANDIDATO VENCEDOR: {vencedor}
    -------------------- ELEIÇÃO --------------------
    - Total de votos Candidato 1: {votos_1} votos
    - Total de votos Candidato 2: {votos_2} votos
    - Total de votos Candidato 3: {votos_3} votos
    - Total de votos nulos: {votos_nulo} votos
    -------------------------------------------------"""

    print(resultado)


if __name__ == '__main__':
    main()