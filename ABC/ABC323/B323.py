N = int(input())

res = []

for i in range(N):
    s = input()
    ct = s.count('o')
    res.append([i + 1, ct])

res.sort(reverse=True, key=lambda x:x[1])
pt = []
for i in res:
    pt.append(i[0])
    
print(*pt)