n, m, p = map(int, input().split())
nl = list(map(int, input().split()) for _ in range(n))
ml = list(map(int, input().split()) for _ in range(m))

ll = []

for i in nl:
    for j in ml:
        ans = i + j
        if ans >= p:
            ans = p
        ll.append(ans)

print(sum(ll))
            

