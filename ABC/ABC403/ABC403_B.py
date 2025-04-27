T = list(input())
U = list(input())

for i in range(len(T)):
    # T[i]がUの最初の文字列と一致するか確認
    if T[i] == U[0] or T[i] == "?":
        res = True
        # T[i]からUの文字列すべて一致しているか確認
        for j in range(len(U)):
            # Tの範囲外を参照しないようにチェック
            if i + j >= len(T) or (T[i + j] != U[j] and T[i + j] != "?"):
                res = False
                break
        # 全て一致している場合はYesを出力
        if res:
            print("Yes")
            exit()

print("No")
