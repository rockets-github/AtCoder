from collections import deque

R, C = map(int, input().split())
S = []
for i in range(R):
    s = input()
    S.append(s)
    
ans = 0

def max_distance(distance):
    max_dist = 0
    
    for dist in distance:
        max_dist = max(max_dist, max(dist))
    
    return max_dist

def BFS(sy, sx):

    #キューの作成
    Q = deque()
    Q.append([sy, sx])
    dist[sy][sx] = 0

    while len(Q) > 0:
        i, j = Q.popleft()
        for i2, j2 in [[i + 1, j],[i - 1, j],[i, j + 1],[i, j - 1]]:
            if not(0 <= i2 < R and 0 <= j2 < C):
                continue
    
            if S[i2][j2] == '#':
                continue
            
            if dist[i2][j2] == -1:
                dist[i2][j2] = dist[i][j] + 1
                Q.append([i2, j2])
    return max_distance(dist)


for i in range(R):
    for j in range(C):
        sy, sx = i, j
        if S[sy][sx] == '#':
            continue
        dist = []
        for i in range(R):
            s = [-1] * C
            dist.append(s)

        ans = max(ans, BFS(sy, sx))


print(ans)