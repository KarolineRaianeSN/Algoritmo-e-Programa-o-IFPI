"""Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
Aritmética que tem por valor inicial A0 e razão R."""
def main():

    a = int(input("Digite o primeiro termo: "))
    ultimo_termo = int(input("Digite o termo limite: "))
    r = int(input("Digite a razão: "))

    #an = a1 + (n - 1)*r
    print(a)
    for i in range(a,ultimo_termo):
        termo = i * r
        if termo <= ultimo_termo:
            print(termo)


main()