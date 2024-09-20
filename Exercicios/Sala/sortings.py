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
def main():
    lista_bagunçada = [1,123,4,2,33,42,78]
    print(bubbleSort(lista_bagunçada))
    print(quickSort(lista_bagunçada))
    print(selectionSort(lista_bagunçada))
    print(lista_bagunçada)


main();