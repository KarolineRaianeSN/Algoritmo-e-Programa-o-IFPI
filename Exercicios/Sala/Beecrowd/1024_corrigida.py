def main():
    n = int(input())
    for _ in range(n):
        palavra = input()
        resultado_primeira_etapa = primeira_etapa(palavra)
        resultado_segunda_etapa = segunda_etapa(resultado_primeira_etapa)
        resultado_terceira_etapa = terceira_etapa(resultado_segunda_etapa)
        print(resultado_terceira_etapa)


def primeira_etapa(palavra):
    resultado_primeira_etapa = ""
    for l in palavra: 
        if l.isalpha():
            if l.islower():
                ordenacao = ord('a') + (ord(l) - ord('a') + 3) % 26
            else:
                ordenacao = ord('A') + (ord(l) - ord('A') + 3) % 26
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
        ordenacao = ord(letra) - 1
        resultado_terceira_etapa += chr(ordenacao)

    return resultado_terceira_etapa


main()