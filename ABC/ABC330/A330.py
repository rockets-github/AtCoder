N, L = map(int,input().split())
pl = list(map(int, input().split()))
res = 0
for i in pl:
    if i >= L:
        res += 1

print(res)