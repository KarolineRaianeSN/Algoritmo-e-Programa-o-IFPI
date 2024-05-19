def main():
    I = 1
    J = 7

    while I <= 9:
        for _ in range(3):
            print("I=" + str(I) + " J=" + str(J))
            J -= 1
        I += 2
        J += 5


main()