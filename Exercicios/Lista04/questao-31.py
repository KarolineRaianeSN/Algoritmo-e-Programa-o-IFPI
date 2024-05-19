def get_number_in_range(prompt, min_value, max_value):
    numero = int(input(prompt))
    while numero < min_value or numero > max_value:
        numero = int(input(prompt))
    return numero

def get_cdu(numero, classe):
    if classe == 'C':
        return numero // 100
    elif classe == 'D':
        return (numero % 100) // 10
    else:
        return (numero % 100) % 10

def to_romano_unidade(numero):
    return ['','I','II','III','IV','V','VI','VII','VIII','IX'][numero]

def to_romano_dezena(numero):
    return ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC'][numero//10]

def to_romano_centena(numero):
    return ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM'][numero//100]

def to_romano(numero):
    if numero < 10:
        return to_romano_unidade(numero)
    elif numero < 100:
        return to_romano_dezena(numero)
    else:
        return to_romano_centena(numero)

def main():
    numero = get_number_in_range('Digite um número: ', 1, 999)

    unidade = get_cdu(numero, 'U')
    dezena = get_cdu(numero, 'D')
    centena = get_cdu(numero, 'C')

    unidade_romano = to_romano(unidade)
    dezena_romano = to_romano(dezena*10)
    centena_romano = to_romano(centena*100)

    numero_romano = centena_romano + dezena_romano + unidade_romano

    print(f'O número {numero} em romano fica {numero_romano}')

main()
