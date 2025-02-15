N, M = map(int, input().split())
p = [set() for _ in range(N)]
ans = 0
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    if x == y:
        ans += 1
        continue

    if y in p[x] or x in p[y]:
        ans += 1
        continue

    p[x].add(y)
    p[y].add(x)

print(ans)
