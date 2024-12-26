import collections

H, W, N = map(int,input().split())
T = list(input())
option = collections.Counter(T)
grid = [list(input()) for _ in range(H)]
move_i = option['D'] - option['U']
move_j = option['R'] - option['L'] 


def move_on(i, j):
    for op in T:
        match op:
            case 'L':
                j -= 1
            case 'R':
                j += 1
            case 'U':
                i -= 1
            case 'D':
                i += 1
        if grid[i][j] == '#':
            return 0
    return 1


ct = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if grid[i][j] == '.':
            ct += move_on(i, j)

print(ct)