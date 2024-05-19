""". Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e
escreva os N termos da PG. Ler o valor de N"""
def main():

    primeiro_termo = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    n = int(input("Número de termos: "))
    termo = primeiro_termo
    i = 0

    while i < n:
        print(termo)
        termo *= razao
        i += 1



main()