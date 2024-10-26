tate = set(range(8))
yoko = set(range(8))

for i in range(8):
    S = list(input())
    for idx, j in enumerate(S):
        if j == "#":
            tate.discard(idx)
            yoko.discard(i)

print(len(yoko) * len(tate))
