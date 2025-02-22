N = int(input())
res = []

for i in range(N):
    s = input()
    res.append([len(s), s])

res.sort()

for i in res:
    print(i[1], end="")
