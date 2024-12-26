def main():
    x, y, z = map(int, input().split())
    num = y * 10 + z

    if num % 4 == 0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()

