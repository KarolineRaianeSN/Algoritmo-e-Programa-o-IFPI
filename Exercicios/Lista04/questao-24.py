def main():

    primeiro_termo = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    n = int(input("Número de termos: "))
    termo = primeiro_termo
    i = 0

    while i < n:
        print(termo)
        termo += razao
        i += 1

main()