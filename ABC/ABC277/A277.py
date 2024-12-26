def main():
    x, y = map(int, input().split())
    n =list(map(int, input().split()))

    if y in n:
        answer = n.index(y)
        print(answer + 1)

if __name__ == '__main__':
    main()
