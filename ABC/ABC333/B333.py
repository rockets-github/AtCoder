
N = list(input())
M = list(input())

dN = abs(ord(N[1]) - ord(N[0]))
dM = abs(ord(M[1]) - ord(M[0]))

if dN == 3:
    dN =2
elif dN == 4:
    dN = 1


if dM == 3:
    dM =2
elif dM == 4:
    dM = 1


if dN == dM:
    print('Yes')
else:
    print('No')