"""
Entrada
Cada caso de teste se estende por várias linhas. A primeira linha contém um inteiro N representando o número de strings no conjunto (1 ≤ N ≤ 104). Cada uma das próximas N linhas contém uma string não-vazia e única com no máximo 1000 caracteres minúsculos do alfabeto inglês. Em cada caso de teste, a soma dos tamanhos das strings é no máximo 106.

O último caso de teste é seguido de uma linha contendo um zero.
Saída
Para cada caso de teste, imprima uma única linha com um único inteiro representando o tamanho da maior sequência de fotos que pode ser produzida.
"""
def maior_sequencia(strings):
    # Crie um dicionário para armazenar o tamanho da maior sequência que pode ser formada até cada string
    dp = {s: 1 for s in strings}

    # Crie um conjunto para armazenar as strings que já foram processadas
    processadas = set()

    # Crie uma lista para armazenar as strings ordenadas por tamanho
    ordenadas = sorted(strings, key=len)

    # Processa cada string
    for s in ordenadas:
        # Se a string já foi processada, pule para a próxima
        if s in processadas:
            continue

        # Marque a string como processada
        processadas.add(s)

        # Verifique todas as strings menores que a atual
        for t in ordenadas:
            # Se a string atual é uma extensão da string menor, atualize o tamanho da sequência
            if len(t) < len(s) and (s.startswith(t) or s.endswith(t)):
                dp[s] = max(dp[s], dp[t] + 1)

    # Retorne o tamanho da maior sequência
    return max(dp.values()) if max(dp.values()) > 1 else 1

# Leitura dos dados
while True:
    n = int(input())
    if n == 0:
        break
    strings = [input() for _ in range(n)]
    print(maior_sequencia(strings))