def main():
    moji = input()
    rya = moji[0] + str(len(moji) - 2) + moji[-1]
    print(rya)


if __name__ == '__main__':
    main()
