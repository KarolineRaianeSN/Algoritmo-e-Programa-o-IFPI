def main():
    N = int(input())
    i = 0

    while i < N:
        a, b, c = map(float, input().split())
        media_ponderada = (a * 2 + b * 3 + c * 5) / 10
        print("%.1f" % media_ponderada)
        i += 1


main()