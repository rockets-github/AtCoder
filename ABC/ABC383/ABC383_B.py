H, W, D = map(int, input().split())
grid = [list(input()) for _ in range(H)]
floors = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == "."]



