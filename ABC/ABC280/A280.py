def main():
    x, y = map(int, input().split())
    print(sum([input().count('#') for _ in range(x)]))


if __name__ == '__main__':
    main()
