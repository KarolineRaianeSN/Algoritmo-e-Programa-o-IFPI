def main():
    arquivo = open("words.txt", "r")


def tamanho_palavra(arquivo):
    linha =  arquivo.readline()
    for linha in arquivo:
        if len(linha) > 5:
            print(linha)
    

main()
