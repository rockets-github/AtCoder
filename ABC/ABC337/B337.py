S = input()

a_c = 0
b_c = 0
c_c = 0

for i in list(S):
    if i == 'A':
        a_c += 1
    if i == 'B':
        b_c += 1
    if i == 'C':
        c_c += 1

res = 'A' * a_c + 'B' * b_c + 'C' * c_c

if S == res:
    print('Yes')
else:
    print('No')