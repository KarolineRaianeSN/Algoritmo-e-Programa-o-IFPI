"""
Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez.
"""
def main():

    nota1 = int(input("Digite a primeira nota: "))
    nota2 = int(input("Digite a segunda nota: "))


    situacao = calc_situacao(nota1, nota2)
    print(f"Você foi {situacao}")

def calc_media(nota1,nota2):
    media = (nota1 + nota2) / 2
    return media

def calc_situacao(nota1,nota2):
    media = calc_media(nota1, nota2)
    if media == 10:
        return "Aprovado com distinção"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

if __name__ == "__main__":
    main()