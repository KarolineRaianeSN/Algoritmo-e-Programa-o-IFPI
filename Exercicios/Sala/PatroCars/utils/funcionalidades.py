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