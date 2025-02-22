N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(N):
    for j in range(i, N):
        if i == j:
            ans += 1
            continue
        
        if i + 1 == j:
            ans += 1
            continue
        
        if A[j] - A[j -1] == A[i + 1] - A[i]:
            ans += 1
        else:
            break



print(ans)