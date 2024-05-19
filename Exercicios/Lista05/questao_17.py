def main():

    n = int(input("Valor de N: "))

    soma = 0

    for i in range(1,n+1):
        soma += 1/i

    print(soma)

main()