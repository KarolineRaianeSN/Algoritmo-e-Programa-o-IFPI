def main():

    pop_cidade_a = 200000
    pop_cidade_b = 800000
    tempo = 0

    while pop_cidade_a < pop_cidade_b:
        pop_cidade_a += pop_cidade_a * 3.5/100
        pop_cidade_b += pop_cidade_b * 1.35/100

        tempo += 1

    print(f"{tempo} anos")


main()