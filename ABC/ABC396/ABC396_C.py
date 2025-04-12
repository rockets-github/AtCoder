N, M = map(int, input().split())

B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

res = 0
b_pos = 0
w_pos = 0


while b_pos < N and B[b_pos] > 0:
    res += B[b_pos]
    b_pos += 1

while w_pos < M and b_pos > w_pos and W[w_pos] > 0:
    res += W[w_pos]
    w_pos += 1


while b_pos < N and w_pos < M:
    if B[b_pos] + W[w_pos] >= 0:
        res += B[b_pos] + W[w_pos]
        b_pos += 1
        w_pos += 1
    else:
        break

print(res)
