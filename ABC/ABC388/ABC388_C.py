from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
res = 0
for i in A:
    target = 2 * i
    index = bisect_left(A, target)
    cnt = N - index
    res += cnt

print(res)