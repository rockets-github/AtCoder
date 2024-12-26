N, L, R = map(int, input().split())
ls = list(map(int,input().split()))
res = []

for i in ls:
    if i >= L and i <= R:
        res.append(i)
    elif i < L:
        res.append(L)
    else:
        res.append(R)
print(*res)
