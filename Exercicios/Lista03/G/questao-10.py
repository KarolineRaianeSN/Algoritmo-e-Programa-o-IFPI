"""
Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media = calc_media(nota1, nota2)
    conceito = calc_conceito(nota1, nota2)
    situacao = calc_situacao(nota1, nota2)
    print(f"""
    Nota 1: {nota1}
    Nota 2: {nota2}
    Média: {media}
    Conceito: {conceito}
    Situação: {situacao}""")

def calc_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


def calc_conceito(nota1, nota2):
    media = calc_media(nota1, nota2)
    if media >= 9:
        return "A"
    elif media >= 7.5:
        return "B"
    elif media >= 6:
        return "C"
    elif media >= 4:
        return "D"
    else:
        return "E"

def calc_situacao(nota1, nota2):
    conceito = calc_conceito(nota1, nota2)
    if conceito == "D" or conceito == "E":
        return "REPROVADO"
    else:
        return "APROVADO"


if __name__ == "__main__":
    main()