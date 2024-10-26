N = int(input())  # おもちゃの数
items = sorted(list(map(int, input().split())), reverse=True)  # おもちゃのサイズ（降順）
boxes = sorted(list(map(int, input().split())), reverse=True)  # 箱のサイズ（降順）

# フラグと変数の初期化
buy = True
size = 0

item_num = 0
box_num = 0

# ループはおもちゃの数に合わせる
while item_num < N:
    # 箱が存在しない、または箱が小さすぎる場合
    if box_num >= len(boxes) or items[item_num] > boxes[box_num]:
        if buy:
            buy = False
            size = items[item_num]  # 新たに購入した箱のサイズは現在のおもちゃのサイズ
        else:
            print(-1)  # もう購入できないなら失敗
            exit()
    else:
        # 箱におもちゃが入る場合、次の箱に進む
        box_num += 1
    
    # 次のおもちゃへ
    item_num += 1

print(size)
