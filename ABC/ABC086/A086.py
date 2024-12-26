def main():
    x, y = map(int, input().split())
    z = x * y
    if z % 2 == 0:
        print('Even')
    else:
        print('Odd')


if __name__ == '__main__':
    main()
