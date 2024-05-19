def main():

    urna = """
    Serra = 45
    Dilma = 13
    Ciro Gomes = 23
    Indeciso = 99
    Outros = 98
    Nulo/Branco = 0
    Fim = -1"""

    print(urna)

    somatorio_serra = 0
    somatorio_dilma = 0
    somatorio_ciro = 0
    somatorio_indeciso = 0
    somatorio_outros = 0
    somatorio_branco = 0
    eleitores = 0

    voto = int(input("Qual o seu voto? "))

    while voto != -1:
        if voto == 45:
            somatorio_serra += 1
        elif voto == 13:
            somatorio_dilma += 1
        elif voto == 23:
            somatorio_ciro += 1
        elif voto == 99:
            somatorio_indeciso += 1
        elif voto == 98:
            somatorio_outros += 1
        elif voto == 0:
            somatorio_branco += 1

        eleitores += 1

        voto = int(input("Qual o seu voto? "))

    porcentagem_serra = (somatorio_serra / eleitores) * 100
    porcentagem_dilma =  (somatorio_dilma / eleitores) * 100
    porcentagem_ciro = (somatorio_ciro / eleitores) * 100
    porcentagem_indeciso = (somatorio_indeciso / eleitores) * 100
    porcentagem_outros = (somatorio_outros / eleitores) * 100
    porcentagem_branco = (somatorio_branco / eleitores) * 100
    resultado = f"""
    Serra: {porcentagem_serra} %
    Dilma: {porcentagem_dilma} %
    Ciro: {porcentagem_ciro} %
    Indecisos: {porcentagem_indeciso} %
    Outros: {porcentagem_outros} %
    Branco: {porcentagem_branco} %"""

    print(resultado)

    if porcentagem_ciro < 50 or porcentagem_serra < 50 or porcentagem_dilma < 50:
        print("Haverá 2º turno")


main()