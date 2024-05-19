def get_number(prompt):
    return int(input(prompt))

def get_number_min(prompt, min_value):
    numero = int(input(prompt))
    while numero < min_value:
        numero = int(input(prompt))
    return numero

def get_positive_number(prompt):
    numero = int(input(prompt))
    while numero < 0:
        numero = int(input(prompt))
    return numero

def computar_carga(quantidade):
    qtd_containers_lidos = 0
    peso_total = 0

    while qtd_containers_lidos < quantidade:
        peso = get_positive_number('Peso Container: ')
        peso_total = peso_total + peso
        qtd_containers_lidos += 1

    return peso_total

def main():
    # Carga
    qtd_containers = get_number_min('Qtd Containers: ', 0)
    peso_carga = computar_carga(qtd_containers)

    # Passageiros
    contador_passageiros = 0
    contador_bagagens = 0
    bilhete = get_number('Bilhete: ')

    while bilhete != 0:
        contador_passageiros += 1
        bagagens = get_number_min('Qtd de Bagagens: ', 0)
        # trabalho
        contador_bagagens += bagagens

        bilhete = get_number('Bilhete: ')

    peso_passageiros = (contador_passageiros * 70) + (contador_bagagens * 10)

    total_peso_fora_combustivel = peso_passageiros + peso_carga
    combustivel_possivel_kg = 500_000 - total_peso_fora_combustivel
    combustivel_possivel_litros = combustivel_possivel_kg / 1.5
    decolagem_autorizada = 'SIM' if combustivel_possivel_litros >= 10_000 else 'NÃO'

    resultado = f"""
    >>>>>>>>> AVIÃO <<<<<<<<<
    - Passageiros Embarcados: {contador_passageiros}
    - total de volume de bagagem: {contador_bagagens}
    - Peso dos Passageiros: {peso_passageiros:.2f}kg
    - Peso da carga: {peso_carga:.2f}kg
    - Decolagem Autorizada? --> {decolagem_autorizada}
    """

    print(resultado)

main()
