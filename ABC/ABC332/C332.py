N, M = map(int,input().split())
S = list(map(int,input()))

new_muji = M
new_logo = 0
used_muji = 0
used_logo = 0


for i in S:

    if i == 0:
        new_muji += used_muji
        used_muji = 0
        new_logo += used_logo
        used_logo = 0
    elif i == 1:
        if new_muji > 0:
            new_muji -= 1
            used_muji += 1
        elif new_logo > 0:
            new_logo -= 1
            used_logo += 1
        else:
            used_logo += 1
    else :
        if new_logo > 0:
            new_logo -= 1
            used_logo += 1
        else:
            used_logo += 1

print(new_logo + used_logo)