import sys

class UnionFind:
    """ Union-Find (Disjoint Set Union) で連結成分を管理 """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
            return True
        return False

def solve():
    # **入力の受け取り**
    N, M = map(int, sys.stdin.readline().split())  # サーバー数, ケーブル数
    edges = []  # (サーバーA, サーバーB, ケーブル番号)
    
    for i in range(M):
        A, B = map(int, sys.stdin.readline().split())
        edges.append((A - 1, B - 1, i + 1))  # 0-indexed に変換
    
    # **現在の接続情報の管理**
    uf = UnionFind(N)
    used_edges = []
    unused_edges = []
    
    for A, B, cable_id in edges:
        if uf.union(A, B):
            used_edges.append((A, B, cable_id))
        else:
            unused_edges.append((A, B, cable_id))  # 余分なケーブル
    
    # **全サーバーを連結するために追加が必要なエッジを探す**
    root_sets = {uf.find(i) for i in range(N)}
    root_list = list(root_sets)
    changes = []

    for i in range(len(root_list) - 1):
        src = root_list[i]
        dest = root_list[i + 1]
        
        if unused_edges:
            # 余っているケーブルを使う
            A, B, cable_id = unused_edges.pop()
            changes.append((cable_id, B + 1, dest + 1))
            uf.union(B, dest)
        else:
            # 余っているケーブルがない場合、手動で変更が必要（エッジ不足）
            print("接続不可能")
            return

    # **出力**
    print(len(changes))
    for cable_id, S, T in changes:
        print(cable_id, S, T)

if __name__ == "__main__":
    solve()
