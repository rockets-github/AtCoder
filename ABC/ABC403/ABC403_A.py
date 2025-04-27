N = int(input())
A = list(map(int, input().split()))

res = 0

#Aの奇数番目を計算
for i in range(0, N, 2):
    res += A[i]

print(res)