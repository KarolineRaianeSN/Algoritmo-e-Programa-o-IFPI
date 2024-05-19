"""
Leia uma letra e verifique se a letra digitada é vogal ou consoante.
"""


def main():
    letra = input("Digite uma letra: ")
    vogal_ou_consoante(letra)


def vogal_ou_consoante(letra):
    vogais = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]

    if letra in vogais:
        return print("É uma vogal")
    else:
        return print("É uma consoante")


if __name__ == "__main__":
    main()
