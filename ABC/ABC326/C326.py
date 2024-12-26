from collections import Counter

N, M = map(int, input().split())
a_l = list(map(int, input().split()))
a_l = sorted(a_l)
c_l = Counter(a_l)
l = set(a_l)
l = list(l)
l = sorted(l)

c_max = 0

for i in range(0, len(l)):
    cm = 0
    for j in range(i, len(l)):
        diff = l[j] - l[i]
        if diff >= M:
            break
        cm += c_l[l[j]]
    c_max = max(c_max, cm)

print(c_max)