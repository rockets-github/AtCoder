def main():
    x, y = map(int, input().split())
    n =list(map(int, input().split()))

    for i in range(y):
        n.pop(0)
        n.append(0)

    print(*n)


if __name__ == '__main__':
    main()