Q = int(input())

res = [0] * 100
for _ in range(Q):
    q = list(map(int, input().split()))

    if q[0] == 1:
        res.append(q[1])
    else:
        print(res.pop())


