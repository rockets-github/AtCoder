import string

alp = list(string.ascii_uppercase)

S = list(input())
res = []

for i in S:
    if i in alp:
        res.append(i)

print(''.join(res))
