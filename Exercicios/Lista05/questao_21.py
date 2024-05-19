def main():

    n = int(input("Valor de N: "))

    soma = 0

    for i in range(1,n+1):
        for j in range(1,n+1,2):
            soma += j/i

    print(soma)

    

main()