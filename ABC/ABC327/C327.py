row_l = [[] for i in range(9)]
col_l = [[] for i in range(9)]
gid_l = [[] for i in range(9)]

res = True

for i in range(9):
    l = list(map(int,input().split()))
    if sum(l) != 45:
        res =False
    else:
        row_l[i] += l
        for j in range(9):
            col_l[j].append(l[j])
        if i < 3:
            gid_l[0] += l[:3]
            gid_l[1] += l[3:6]
            gid_l[2] += l[6:9]
        elif i < 6:
            gid_l[3] += l[:3]
            gid_l[4] += l[3:6]
            gid_l[5] += l[6:9]
        else:
            gid_l[6] += l[:3]
            gid_l[7] += l[3:6]
            gid_l[8] += l[6:9]


for i in range(9):
    if sum(col_l[i]) != 45:
        res = False
    if (sum(gid_l[i]) != 45):
        res = False


if res:
    print('Yes')
else:
    print('No')
