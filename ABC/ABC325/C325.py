H, W = map(int, input().split())
maze = [list(input()) for _ in range (H)]
res = [[False] * W for _ in range(H)] 

cnt = 0

def tf(i, j):
    if maze[i][j] == '#':
        res[i][j] = True
    p = True
    for y, x in [[i - 1, j], [i - 1, j + 1], [i, j + 1], [i + 1, j + 1], [i + 1, j], [i + 1, j - 1], [i, j - 1], [i - 1, j - 1]]:
        if (y < H and 0 <= y) and (x < W  and 0 <= x):
            if maze[y][x] == '#':
                if res[y][x] == True:
                    p = False
                else:
                    res[y][x] = True
            tf(y, x)
    if p:
        cnt += 1

for i in range(H):
    for j in range(W):
        tf(i, j)




print(cnt)