N, M = map(int, input().split())
A = set(map(int, input().split()))
result = []

for i in range(1, N+1):
    if i not in A:
        result.append(i)

print(len(result))
print(*result)


