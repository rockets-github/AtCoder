N = int(input())
result = 0
past_time = 0

for i in range(N):
    T, V = map(int, input().split())
    result = max(0, result - (T-past_time))
    result += V
    past_time = T

print(result)