N, K = map(int, input().split())
MOD = 10**9

A = [1] * K

current_sum = K


for i in range(K, N + 1):
    next_val = current_sum % MOD
    A.append(next_val)
    current_sum += next_val - A[i-K]

print(A[N])
