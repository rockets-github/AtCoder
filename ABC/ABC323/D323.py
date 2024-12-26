from collections import defaultdict
import copy

N = int(input())

cSlime = defaultdict(str)
resSlime = defaultdict(str)

for i in range(N):
    s, m = input().split()
    cSlime[s] = int(m)

cK = list(cSlime.keys())

for i in cK:

    di = str(int(i) * 2)
    print(cSlime[i] % 2)

    if di not in cSlime:
    # キーが存在しない場合の処理
        cSlime[di] = 0
        
    while cSlime[i] > 1:
        cSlime[i] = int(cSlime[i] % 2)
        cSlime[di] += int(cSlime[i] // 2)
        print(cSlime[di])
        cSlime[di] += 5
        print(cSlime)
        print(cSlime[di])

