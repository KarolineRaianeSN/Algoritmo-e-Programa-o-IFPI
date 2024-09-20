def bubbleSort(lista):
    # Cria uma cópia da lista, desnecessário
    lista = lista[:]
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    
    return lista;

def quickSort(lista):
    if len(lista) < 2:
        return lista;

    pivot = lista[0]
    left = [i for i in lista[1:] if i < pivot]
    right = [i for i in lista[1:] if i >= pivot]
    return quickSort(left)+[pivot]+quickSort(right)


def selectionSort(lista):
    lista = lista[:]
    if len(lista) < 2:
        return lista

    for i in range(len(lista)-1):
        menor = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[menor]:
                menor = j
        
        if lista[i] != lista[menor]:
            lista[i], lista[menor] = lista[menor], lista[i]

    return lista

def busca_sequencial(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i  # Retorna o índice onde o valor foi encontrado
    return -1  # Retorna -1 se o valor não for encontrado

# Exemplo de uso
lista = [10, 23, 45, 70, 11, 15]
resultado = busca_sequencial(lista, 70)  # Retorna 3
print(resultado)


def busca_binaria(lista, valor):
    esquerda = 0
    direita = len(lista) - 1
    
    while esquerda <= direita:
        meio = (esquerda + direita) // 2  # Encontra o elemento do meio
        
        # Verifica se o valor está no meio
        if lista[meio] == valor:
            return meio
        
        # Se o valor procurado for menor, busca na metade esquerda
        elif lista[meio] > valor:
            direita = meio - 1
        
        # Se o valor procurado for maior, busca na metade direita
        else:
            esquerda = meio + 1
    
    return -1  # Retorna -1 se o valor não for encontrado

# Exemplo de uso
lista = [10, 23, 45, 70, 89, 95]
resultado = busca_binaria(lista, 70)  # Retorna 3
print(resultado)




def main():
    lista_bagunçada = [1,123,4,2,33,42,78]
    print(bubbleSort(lista_bagunçada))
    print(quickSort(lista_bagunçada))
    print(selectionSort(lista_bagunçada))
    print(lista_bagunçada)


main();