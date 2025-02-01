N, W = map(int, input().split())
block = [[] for _ in range(W)]

c1 = 0
for no, _ in enumerate(range(N)):
    pos, x = map(int, input().split())
    pos -= 1
    block[pos].append(no)

    if x == 1:
        c1 += 1


min_time = N
for i in block:
    min_time = min(min_time, len(i))


block_exit = [True] * N


time_L = []
time_L.append(block_exit)

if c1 != W:
    time_L.append(block_exit)


for i in range(min_time):
    l = block_exit.copy()

    for j in block:
        l[j[i]] = False

    time_L.append(l)



Q = int(input())

min_time = len(time_L) - 1


for t in range(Q):
    query_t, query_num = list(map(int, input().split()))
    
    query_t = min(query_t, min_time)
    
    if time_L[query_t][query_num - 1]:
        print('Yes')
    else:
        print('No')