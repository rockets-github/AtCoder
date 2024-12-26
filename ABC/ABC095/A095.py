def main():
    num = input()
    c_num = 700
    if num[0] == 'o':
        c_num += 100
    if num[1] == 'o':
        c_num += 100
    if num[2] == 'o':
        c_num += 100
    print(c_num)


if __name__ == '__main__':
    main()
