def main():
    N = int(input())

    i = 1

    while i <= 10000:
        if i % N == 2:
            print(i)
        i += 1


if __name__ == '__main__':
    main()