numeros = [9, 1, 8, 2, 7, 3, 6, 4, 2, 5]

def quicksort(l, criterio= lambda x:x, reverse=False) -> list: 
    """ Ordena números de acordo com uma função lambda, podendo ser em ordem crescente ou decrescente"""

    if len(l) < 2:
        return l
    else:
        pivot = l[0]
        menores = [i for i in l[1:] if criterio(i) < criterio(pivot)]
        maiores = [i for i in l[1:] if criterio(i) >= criterio(pivot)]
        return quicksort(menores, criterio, reverse) + [pivot] + quicksort(maiores, criterio, reverse)

numeros_ordenados = quicksort(numeros)
print(numeros_ordenados)