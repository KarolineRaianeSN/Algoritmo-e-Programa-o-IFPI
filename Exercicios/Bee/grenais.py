def main():
    grenais = 0
    inter_vitorias = 0
    gremio_vitorias = 0
    empates = 0

    while True:
        inter_gols, gremio_gols = map(int, input().split())

        grenais += 1

        if inter_gols > gremio_gols:
            inter_vitorias += 1
        elif gremio_gols > inter_gols:
            gremio_vitorias += 1
        else:
            empates += 1

        print("Novo grenal (1-sim 2-nao)")
        opcao = int(input())

        if opcao == 2:
            break

    print("{} grenais".format(grenais))
    print("Inter:{}".format(inter_vitorias))
    print("Gremio:{}".format(gremio_vitorias))
    print("Empates:{}".format(empates))

    if inter_vitorias > gremio_vitorias:
        print("Inter venceu mais")
    elif gremio_vitorias > inter_vitorias:
        print("Gremio venceu mais")
    else:
        print("Nao houve vencedor")


main()