N = int(input())
S = input()
C = range(N)
cost = []

for i in range(len(S)):
    if S[i] == "1":
        cost.append(C[i])

if len(cost) == 0:
    print(0)

# スタート位置を決定
s = len(cost) // 2

mid = cost[s]
ans = 0
l = 0
r = 0

for i in range(len(cost)):

    if s == i:
        continue
    if i > s:
        r += 1
        calc = cost[i] - mid- r
    else:
        l += 1
        calc = mid - cost[i]- l
    ans += calc

print(ans)


# N = int(input())
# S = input()

# # 1 の位置を取得
# ones = [i for i, c in enumerate(S) if c == "1"]
# m = len(ones)  # 1 の個数

# # 中央値を求める
# median_idx = m // 2
# median = ones[median_idx]

# # 各 1 を中央値に寄せるための移動コストを求める
# ans = 0

# for i in range(m):
#     ans += abs(ones[i] - median - (i - median_idx))

# print(ans)
