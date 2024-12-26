n, t = map(int, input().split())
car = list(map(int, input().split()))
num = list(map(int, input().split()))

if t not in car:
    t = car[0]

res = 0
p_num = 0

for i in range(n):
    if t == car[i] and res < num[i]:
        res = num[i]
        p_num = i + 1
        
print(p_num)
