Q = int(input())

# Queryの種類
# 1 X: 待ち行列の末尾に 1人並ぶ。このとき並ぶ人はメニュー番号が X の食券を持って並ぶ。
#2: 待ち行列の先頭にいる人をレストランに案内する。このとき案内される人が持っている食券のメニュー番号を出力する。

# 待ち行列
queue = []

for i in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        queue.append(query[1])
    elif query[0] == 2:
        print(queue.pop(0))

