def main():
    N = int(input())

    i = 1

    while i <= N:
        print(i, i * i, i * i * i)
        print(i, i * i + 1, i * i * i + 1)
        i += 1


main()