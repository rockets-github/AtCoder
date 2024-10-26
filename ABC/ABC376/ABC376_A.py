N, C = map(int, input().split())
T = list(map(int, input().split()))

before_get_time = 0
res = 0
for i in range(len(T)):
    ct = T[i] - before_get_time
    if i == 0 or C <= ct:
        res += 1
        before_get_time = T[i]

print(res)
