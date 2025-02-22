import heapq

N = int(input())
G = [[] for _ in range(N)]


for i in range(N):
    s = list(input())
    print(s)
    for j in range(N):
        if i != j and s[j] != "-":
            print(j)
            G[i].append((j, s[j]))


print(G)

dist = [[-1]*N for _ in range(N)]

print(dist)

Q = []
h, w = 0, 0
heapq.heappush(Q, (0, h, w))

dist[h][w] = 0




# done = [False]*N

# while len(Q)> 0:
#     d, h, w = heapq.heappop(Q)
    
#     if done[i]:
#         continue
    
#     done[i] = True
    
#     for j, c in G[i]:
        
#         if dist[i] == -1 or dist[j] + c:
#             dist[j] = dist[i] + c
#             heapq.heappush(Q, (dist[j], j))

# print(pass)
