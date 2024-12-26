N = int(input())
# 通常
if N % 2 == 0:
    print(N // 2)
else:
    print(N // 2 + 1)

# 切り上げ割り算 (a + b -1) // b
print((N + 2 - 1) // 2)

# 一行
print((int(input()) + 2 - 1) // 2)