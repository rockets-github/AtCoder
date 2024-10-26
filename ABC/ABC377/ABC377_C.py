def check_mate(occupied_cells, y, x, N):
    moves = [(2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2)]

    for dy, dx in moves:
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < N:
            occupied_cells.add((ny, nx))


N, M = map(int, input().split())
occupied_cells = set()
for _ in range(M):
    y, x = map(int, input().split())
    check_mate(occupied_cells, y - 1, x - 1, N)


result = N * N - len(occupied_cells)
print(result)
