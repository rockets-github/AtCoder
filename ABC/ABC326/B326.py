from collections import defaultdict
ln  = defaultdict(int)

cnt = 0
for i in range(1, 10):
    for j in range(0, 10):
        x = i * j
        if x < 10:
            str_num = int(str(i) + str(j) + str(x))
            ln[cnt] = str_num
            cnt += 1

N = int(input())

for v in ln.values():
    if N <= v:
        print(v)
        exit()
