from collections import defaultdict


N = int(input())
K = []
A = []
P = []


for _ in range(N):
    data = list(map(int, input().split()))
    values = data[1:]
    K.append(data[0])
    A.append(values)


for i in range(N):
    p = defaultdict(float)
    for j in A[i]:
        p[j] += 1 / K[i]
    P.append(p)

max_p = 0
for i in range(N):
    for j in range(i + 1, N):
        p_i = P[i]
        p_j = P[j]
        common_p = sum(p_i[x] * p_j[x] for x in p_i if x in p_j)
        max_p = max(max_p, common_p)

print(max_p)
