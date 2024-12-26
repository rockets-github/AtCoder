import itertools

m = int(input()) - 1
n = []

for i in range(1, 13):

    n.append(int("1" * i))



cr = list(map(sum,itertools.combinations_with_replacement(n, 3)))

cr.sort()

print(cr[m])