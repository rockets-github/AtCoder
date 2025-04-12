from collections import deque

# 入力を処理
N, M = map(int, input().split())

edges = []
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))  # 0-based index
    graph[u - 1].append((v - 1, w))
    graph[v - 1].append((u - 1, w))

# 各頂点の値を管理
A = [-1] * N  # -1 なら未訪問
basis = []  # XOR基底

# BFS で探索（DFSだとスタックオーバーフローの可能性）
queue = deque([(0, 0)])  # (頂点, XOR値)
A[0] = 0

cnt = 0  # 進捗確認用
while queue:
    v, xor_val = queue.popleft()
    cnt += 1
    for nv, w in graph[v]:
        if A[nv] == -1:
            # 未訪問なら値を設定
            A[nv] = xor_val ^ w
            queue.append((nv, A[nv]))
        else:
            # 矛盾の確認
            new_val = A[nv] ^ xor_val ^ w
            if new_val:
                basis.append(new_val)  # XOR基底に追加


# XOR 基底のガウス消去（O(60^2) で十分高速）
def insert_basis(x):
    for b in sorted(basis, reverse=True):
        x = min(x, x ^ b)
    if x:
        basis.append(x)


# 基底を整理
new_basis = []
for x in basis:
    insert_basis(x)
basis = new_basis

# A の最適化
min_xor = 0
for b in basis:
    min_xor = min(min_xor, min_xor ^ b)

# A の値を最適化
for i in range(N):
    A[i] ^= min_xor

# 結果を出力
print(*A)
