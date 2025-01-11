N, D = map(int, input().split())

snake = []
for i in range(N):
    T, L = map(int, input().split())
    snake.append((T, L))

for i in range(1, D+1):
    max_L = 0
    for j in snake:
        max_L = max(max_L, j[0] * (j[1]+i))
    print(max_L)