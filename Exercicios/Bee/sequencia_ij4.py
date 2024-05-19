def main():
    import decimal

    df = decimal.Decimal

    for i in range(0, 201, 20):
        for j in range(1, 11):
            if i == 0 or i == 100 or i == 200:
                print(f'I={i} J={j}')
            elif i % 10 == 0:
                print(f'I={i / 10:.0f} J={j}')
            else:
                print(f'I={i / 10:.1f} J={j}')
if __name__ == '__main__':
    main()