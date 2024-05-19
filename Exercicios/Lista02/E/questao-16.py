"""
Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média
final. Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve
escreva “Reprovado”.
"""
def main():
    notaA = int(input("Digite a primeira nota: "))
    notaB = int(input("Digite a segunda nota: "))

    resultado = print(f"BOLETIM:\n"
             f"Nota 1=  {notaA}\n "
             f"Nota 2: {notaB}\n"
             f"-----------------\n"
             f"Média       : {media(notaA,notaB)}\n"
             f"Situação    : {situacao(notaA,notaB)}\n")


def media(notaA,notaB):
    media = (notaA + notaB) / 2
    return media


def situacao(notaA,notaB):
    if media(notaA,notaB) >= 7:
        return "Aprovado"
    elif media(notaA,notaB) >=5:
        return final(notaA,notaB)
    else:
        return "Reprovado"



def final(notaA,notaB):
    print(f"Você ficou de prova final com média {media(notaA,notaB)}")
    prova_final = int(input("Digite a nota da prova final: "))
    media_com_final = (media(notaA,notaB) + prova_final) / 2
    if media_com_final >= 5:
        return print(f"Aprovado com média {media_com_final}")
    else:
        return print(f"Reprovado com média {media_com_final}")


if __name__ == "__main__":
    main()
