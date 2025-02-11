H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

t = 1000
b = 0
l = 1000
r = 0

for h in range(H):
    for w in range(W):
        if grid[h][w] == "#":
            t = min(t, h)
            b = max(b, h)
            l = min(l, w)
            r = max(r, w)


for h in range(t, b + 1):
    for w in range(l, r + 1):
        if grid[h][w] == ".":
            print('No')
            exit()

print('Yes')