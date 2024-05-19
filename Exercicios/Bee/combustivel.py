def main():

    tempo = float(input())
    velocidade = float(input())

    distancia = tempo * velocidade
    combustivel = distancia / 12

    print(f"{combustivel:.3f}")

main()