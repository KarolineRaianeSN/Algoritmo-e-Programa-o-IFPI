"""Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita, segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada, a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada) devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'."""

def main():
    palavra_passe = input("Palavra-passe: ")

    resultado_primeira_etapa = primeira_etapa(palavra_passe)
    resultado_segunda_etapa = segunda_etapa(resultado_primeira_etapa)
    resultado_terceira_etapa = terceira_etapa(resultado_segunda_etapa)

    print(resultado_terceira_etapa)


def letra(letra):
        return ord(letra) >= 65 and ord(letra) <= 90 or ord(letra) >= 97 and ord(letra) <= 122


def primeira_etapa(palavra):
    resultado_primeira_etapa = ""
    for l in palavra: 
        if letra(l):
            ordenacao = int(ord(l)) + 3
            resultado_primeira_etapa += chr(ordenacao)
        else:
             resultado_primeira_etapa += l

    return resultado_primeira_etapa 


def segunda_etapa(palavra):
     return palavra[::-1]


def terceira_etapa(palavra):
    meio = len(palavra) //2
    primeira_metade = palavra[:meio]
    segunda_metade = palavra[meio:]
    resultado_terceira_etapa = primeira_metade


    for letra in segunda_metade:
        ordenacao = int(ord(letra)) - 1
        resultado_terceira_etapa += chr(ordenacao)

    return resultado_terceira_etapa


main()