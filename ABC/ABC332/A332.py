N, S, K = map(int,input().split())

sum = 0

for i in range(N):
    price, buy = map(int,input().split())
    sum = sum + (price * buy)

if sum >= S :
    print(sum)
else:
    print(sum + K)