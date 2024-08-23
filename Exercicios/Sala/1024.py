def tres_para_direita(texto):
    novo_texto = "";
    for carac in texto:
        # se for uma letra
        if (ord(carac) > 64 and ord (carac) < 91) or (ord(carac) > 96 and ord(carac) < 123):
            novo_texto += chr(ord(carac) + 3); # adiciona o caractere com 3 casas deslocadas à esquerda
            continue;

        novo_texto += carac; # adiciona o caractere normal, se não for uma letra.

    return novo_texto;


def inverter(texto):
    # devolve o texto invertido, ao percorrer ele ao contrário, devido ao -1
    return texto[::-1];



def metade_para_esquerda(texto):
    novo_texto = "";

    metade = len(texto)//2; # metade do tamanho da string

    # para cada caractere do meio do texto pra frente
    for carac in texto[metade:]:
        # adiciona o caractere com um caractere deslocado para a esquerda na tabela ascii
        novo_texto += chr(ord(carac) - 1);

    # devolve a metade inicial do texto concatenada com o texto que foi deslocado
    return texto[:metade] + novo_texto;

def main():
    num = int(input()); # quantidade de inputs
    
    for i in range(num):
        entrada = input(); # entrada
        # desloca letras maiúsculas e minusculas 3 carac. à frente na tab ascii
        entrada = tres_para_direita(entrada);
        
        # inverte a linha;
        entrada = inverter(entrada);
        
        # todos os caracteres a partir da metade da string são
        # deslocados para a esquerda em 1 caractere na tabela ascii
        entrada = metade_para_esquerda(entrada);
        
        print(entrada); # exibe a string totalmente modificada


main();