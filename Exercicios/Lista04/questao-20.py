"""Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado
um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
· Distância percorrida desde a última medição;
· Quantidade de litros consumidos para percorrer a distância indicada.
Escreva um algoritmo que leia estas informações e escreva:
· se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
· se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
· o consumo em km/l do carro."""
def main():

    distancia_percorrida = 0
    combustivel_consumido = 0

    while distancia_percorrida < 600 and combustivel_consumido < 50:

        distancia = int(input("Distância percorrida: "))
        combustivel = int(input("Combustível gasto: "))

        distancia_percorrida += distancia
        combustivel_consumido += combustivel

    if distancia_percorrida >= 600:
        print("Você chegou ao seu destino")
    elif combustivel_consumido >= 50:
        print("Você parou por falta de combustível")

    consumo = distancia_percorrida / combustivel_consumido
    print(f"O consumo do carro foi de {consumo} km/l")









main()