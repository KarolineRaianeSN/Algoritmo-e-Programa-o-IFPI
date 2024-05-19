def main():

    N = int(input())

    i = 1

    while i <= N:
        if i % 2 == 0:
            quadrado = i * i
            print(f"{i}^2 = {quadrado}")
        i += 1


main()