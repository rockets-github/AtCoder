from collections import defaultdict
import sys
import copy
sys.setrecursionlimit(10**5+10)

N, M = map(int, input().split())
cM = list(map(int, input().split()))
players = list(list(input()) for _ in range(N))

# print(N)
# print(M)
# print(cM)
# print(players)


#各プレイヤー総合得点の集計
cPlayers = defaultdict(int)

for i in range(len(players)):
    for j in range(len(players[i])):
        if players[i][j] == 'o':
            cPlayers[i] = cPlayers[i] + cM[j]
    cPlayers[i] = cPlayers[i] + i

# print(cPlayers)
# defaultdict(<class 'int'>, {0: 2000, 1: 1500, 2: 1700}

#　合計値取得
pMax = max(cPlayers.values())
# print(pMax)

def cRes(i, j, ct, ctList):
    if j >= pMax:
        print(ct)
    else:
        p = max(ctList)
        ind = ctList.index(p)

        if players[i][ind] == 'x':
            j += p
            ctList[ind] = 0
            ct += 1
        else:
            ctList[ind] = 0

        # cRes呼び出し
        cRes(i, j, ct, ctList)

#各プレイヤーの勝ち点計算
for i, j in cPlayers.items():
    ct = 0
    ctList = copy.copy(cM)
    cRes(i, j, ct, ctList)






    
