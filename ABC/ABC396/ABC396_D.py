N, M = map(int, input().split())

dpath = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, w = map(int, input().split())
    dpath[u].append((v, w))
    dpath[v].append((u, w))

visited = [False] * (N + 1)
xor_values = []
min_xor = float('inf')

def dfs(node, current_xor):
    global min_xor

    if node == N:
        min_xor = min(min_xor, current_xor)
        return

    visited[node] = True
    for neighbor, weight in dpath[node]:
        if not visited[neighbor]:
            dfs(neighbor, current_xor ^ weight)

    visited[node] = False

dfs(1, 0)

print(min_xor)
