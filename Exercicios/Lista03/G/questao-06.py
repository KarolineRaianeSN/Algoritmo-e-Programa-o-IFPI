"""
Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e
escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

def main():

    menu()
    turno = input("Digite a sigla do seu turno: ")
    saudacao = mensagem(turno)
    print(saudacao)
def menu():
    print("""
    M - Matutino
    V - Vespertino
    N - Noturno""")


def mensagem(turno):
    if turno == "M":
        return "Bom dia!"
    elif turno == "V":
        return "Boa tarde!"
    elif turno == "V":
        return "Boa noite!"
    else:
        return "Valor inválido"

if __name__ == "__main__":
    main()