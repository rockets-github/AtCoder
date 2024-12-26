def main():
    num = input()
    c_num = 0
    if num[0] == '1':
        c_num += 1
    if num[1] == '1':
        c_num += 1
    if num[2] == '1':
        c_num += 1
    print(c_num)


if __name__ == '__main__':
    main()