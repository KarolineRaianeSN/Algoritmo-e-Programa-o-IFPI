def main():

    aprovados = 0
    reprovados = 0
    alunos = 0
    while True:
        matricula = int(input("Matrícula: "))
        if matricula == 0:
            break

        nota1 = int(input("Nota 1: "))
        nota2 = int(input("Nota 2: "))
        nota3 = int(input("Nota 3: "))

        media = calc_media(nota1, nota2, nota3)
        situacao = calc_situacao(media)

        if situacao == "Aprovado":
            aprovados += 1
        else:
            reprovados += 1

        alunos += 1

    resultado = (f"""  Total de alunos: {alunos}
                       Aprovados: {aprovados}
                       Reprovados: {reprovados} """)
    print(resultado)
def calc_media (nota1, nota2, nota3):
    return (nota1 *2 + nota2 *3 + nota3 *5 ) / 10


def calc_situacao(media):
    return "Aprovado" if media > 7 else "Reprovado"


main()