def main():
    x = int(input())
    y = int(input())

    if x < y:
        start, end = x, y
    else:
        start, end = y, x

    i = start
    while i <= end:
        if i % 5 == 2 or i % 5 == 3:
            print(i)
        i += 1


main()