def a300():
    n, x, y = map(int,input().split())
    ans = x + y
    opt = list(map(int, input().split()))
    for i, j in enumerate(opt, 1):
        if ans == j:
            print(i)
            break


if __name__ == '__main__':
    a300()



