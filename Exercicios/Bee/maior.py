def main():
    numeros_ins = input()

    numeros_sep = numeros_ins.split(" ")
    a = int(numeros_sep[0])
    b = int(numeros_sep[1])
    c = int(numeros_sep[2])

    maior = (a + b + abs(a - b)) / 2
    maior_final = maior = ((maior + c + abs(maior - c)) / 2)

    print(f"{maior} eh o maior")


main()