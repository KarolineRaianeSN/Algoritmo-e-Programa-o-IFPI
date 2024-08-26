import random

def mostrar_valores(vetor):
    print("Valores no vetor:", vetor)

def resetar_vetor(vetor, valor_padrao):
    vetor.clear()
    vetor.extend([valor_padrao])

def quantidade_itens(vetor):
    return len(vetor)

def menor_maior_valores(vetor):
    return min(vetor), max(vetor)

def somatorio_valores(vetor):
    return sum(vetor)

def media_valores(vetor):
    return sum(vetor) / len(vetor) if vetor else 0

def valores_positivos(vetor):
    positivos = [v for v in vetor if v > 0]
    return positivos, len(positivos)

def valores_negativos(vetor):
    negativos = [v for v in vetor if v < 0]
    return negativos, len(negativos)

def multiplicar_valores(vetor, multiplicador):
    return [v * multiplicador for v in vetor]

def elevar_valores(vetor, expoente):
    return [v ** expoente for v in vetor]

def reduzir_por_fracao(vetor, fracao):
    return [v * fracao for v in vetor]

def substituir_negativos(vetor, min_val, max_val):
    return [random.randint(min_val, max_val) if v < 0 else v for v in vetor]

def ordenar_valores(vetor, reverse=False):
    return sorted(vetor, reverse=reverse)

def embaralhar_valores(vetor):
    random.shuffle(vetor)
    return vetor

