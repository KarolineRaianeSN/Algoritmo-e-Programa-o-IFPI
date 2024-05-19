def main():
    numero_prova = 0
    qtd_nadadores = 0
    total_pontos_a, total_pontos_b = 0, 0
    numero_prova = int(input("Digite o número da prova: "))
    qtd_nadadores = int(input("Digite o número de nadadores: "))
    pontos_a, pontos_b = prova(qtd_nadadores)
    total_pontos_a += pontos_a
    total_pontos_b += pontos_b

    while qtd_nadadores != 0:
        numero_prova = int(input("Digite o número da prova: "))
        qtd_nadadores = int(input("Digite o número de nadadores: "))


        pontos_a, pontos_b = prova(qtd_nadadores)
        total_pontos_a += pontos_a
        total_pontos_b += pontos_b

    if total_pontos_a > total_pontos_b:
        print(f"Vencedor Clube A com {total_pontos_a} pontos")
    elif total_pontos_b > total_pontos_b:
        print(f"Vencedor Clube B com {total_pontos_b}")
    else:
        print("Empate")

def prova(qtd_nadadores):
    nadadores = qtd_nadadores
    total_pontos_a = 0
    total_pontos_b = 0
    print(qtd_nadadores)
    while nadadores > 0:
        nome = input("Nome do nadador: ")
        classificacao = input("Classificação: ")
        tempo = input("Tempo: ")
        clube = input("Clube (a ou b): ")

        pontos_a,pontos_b = calc_pontuacao(classificacao,clube)
        total_pontos_a += pontos_a
        total_pontos_b += pontos_b

        nadadores -= 1


    return total_pontos_a, total_pontos_b


def calc_pontuacao(classificacao, clube):
    pontos_a = 0
    pontos_b = 0
    if clube == "a":
        if classificacao == "1":
            pontos_a += 9
        elif classificacao == "2":
            pontos_a += 6
        elif classificacao == "3":
            pontos_a += 4
        elif classificacao == "4":
            pontos_a += 3
        else:
            pontos_a += 0
    else:
        if classificacao == "1":
            pontos_b += 9
        elif classificacao == "2":
            pontos_b += 6
        elif classificacao == "3":
            pontos_b += 4
        elif classificacao == "4":
            pontos_b += 3
        else:
            pontos_b += 0

    return pontos_a, pontos_b

main()