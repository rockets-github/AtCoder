N, X = map(int,input().split())
p_l = list(map(int, input().split()))
p_l.sort()
res = 0

for i in p_l:
    if i <= X:
        res += i
    else:
        continue
print(res)
