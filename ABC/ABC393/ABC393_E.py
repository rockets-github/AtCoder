import sys
import math

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

MAX_A = 10**6
f = [0] * (MAX_A + 1)
gc = [0] * (MAX_A + 1)

for x in A:
    f[x] += 1

for g in range(1, MAX_A + 1):
    for m in range(g, MAX_A + 1, g):
        gc[g] += f[m]

result = []
for x in A:
    best = 1
    sqrt_x = int(math.sqrt(x))

    for g in range(1, sqrt_x + 1):
        if x % g == 0:
            if gc[g] >= K:
                best = max(best, g)
            if gc[x // g] >= K:
                best = max(best, x // g)

    result.append(str(best))

sys.stdout.write("\n".join(result) + "\n")
