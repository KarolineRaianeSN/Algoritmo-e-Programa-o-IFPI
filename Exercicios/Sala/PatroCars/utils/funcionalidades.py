import os
import sys
import platform
from utils.ulid import *

def limpar_tela():
    sistema = platform.system()

    if sistema == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def pedir_numero(texto):
    return int(input(texto))


def pedir_numero_positivo(texto):
    numero = int(input(texto))
    while numero <= 0:
        print("Informe um número positivo.")
        numero = float(input(texto))
    return numero


def ordenar_lista(lista, ordenar_por, ordenacao):
    if len(lista) <= 1:
        return lista

    pivot = lista[len(lista) // 2][ordenar_por]
    if ordenacao == "asc":
        left = [x for x in lista if x[ordenar_por] < pivot]
        middle = [x for x in lista if x[ordenar_por] == pivot]
        right = [x for x in lista if x[ordenar_por] > pivot]
        return ordenar_lista(left, ordenar_por, ordenacao) + middle + ordenar_lista(right, ordenar_por, ordenacao)
    elif ordenacao == "desc":
        left = [x for x in lista if x[ordenar_por] > pivot]
        middle = [x for x in lista if x[ordenar_por] == pivot]
        right = [x for x in lista if x[ordenar_por] < pivot]
        return ordenar_lista(left, ordenar_por, ordenacao) + middle + ordenar_lista(right, ordenar_por, ordenacao)
    else:
        print("Ordenação inválida")
        return lista
    

    