from collections import defaultdict

N, M = map(int, input().split())
K = [set() for _ in range(M+1)] 
ingredients = defaultdict(list) 

for i in range(1, M+1):
    K_l = list(map(int, input().split()))
    K[i] = set(K_l[1:])
    for j in K_l[1:]:
        ingredients[j].append(i)

B = list(map(int, input().split()))
ct = 0

for value in B:
    for j in ingredients[value]:
        K[j].remove(value)
        if not K[j]:
            ct += 1
    print(ct)


