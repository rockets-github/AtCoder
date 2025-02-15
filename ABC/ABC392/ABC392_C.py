N = int(input())

P = list(map(int, input().split()))
Q = list(map(int, input().split()))


Z = [0] *  N

for p, q in zip(P, Q):
    p -= 1
    q -= 1
    
    Z[q] = Q[p]

print(*Z)
         

