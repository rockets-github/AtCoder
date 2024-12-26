N, S, M, L = map(int,input().split())

dp = [0] + [float('inf')] * (N + 12)

for i in range(N + 12):
    if i >= 6:
        dp[i] = min(dp[i], dp[i - 6] + S)
    if i >= 8:
        dp[i] = min(dp[i], dp[i - 8] + M)
    if i >= 12:
        dp[i] = min(dp[i], dp[i - 12] + L)

print(min(dp[N:]))