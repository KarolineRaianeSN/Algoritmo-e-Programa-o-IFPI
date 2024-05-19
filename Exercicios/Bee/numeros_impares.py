def main():

    X = int(input())
    if X % 2 == 0:
        X += 1

    cont = 0
    while cont < 6:
        print(X)
        X += 2
        cont += 1

main()