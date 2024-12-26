# 通常
N = int(input())
if N % 3 == 0:
    print('YES')
else:
    print('NO')

#　三項演算子を用いた方法
print('YES' if int(input()) % 3 == 0 else 'NO')