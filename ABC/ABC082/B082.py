def main():
    n = list(input())
    m = list(input())
    n.sort()
    m.sort(reverse=True)
    result = True
    if len(n) < len(m):
        for i in range(len(n)):
            if n[i] != m[i]:
                result = False

    for i in range(len(n)):
        if n[i] == m[i]:
            continue
        elif n[i] < m[i]:
            result = True
            break

    if result:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
