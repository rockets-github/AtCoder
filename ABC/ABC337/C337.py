N = int(input())
l = list(map(int, input().split()))
d = {}

for i in range(1, N + 1):
    d[l[i - 1]] = i

key = -1
res = []
for i in range(N):
    res.append(d[key])
    key = d[key]

print(*res)