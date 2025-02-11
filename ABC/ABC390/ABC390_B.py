N = int(input())
A = list(map(int, input().split()))


flag = True
for i in range(N - 2):
    if (A[i+1] * A[i+1]) != (A[i] * A[i + 2]):
        flag = False

print("Yes" if flag else "No")
