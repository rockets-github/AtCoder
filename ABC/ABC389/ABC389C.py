from collections import deque

Q = int(input())
d = deque()
last_add = 0

for i in range(Q):
    q = input()
    if len(q) == 1:
        d.popleft()
    else:
        q_num, q_length = map(int, q.split())
        if q_num == 1:
            d.append(last_add)
            last_add += q_length
        else:
            print(d[q_length - 1] - d[0])
