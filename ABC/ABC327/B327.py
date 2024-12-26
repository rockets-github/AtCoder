B = int(input())

res = -1
x = 1
xx = 1
while xx <= B :
    xx = x**x
    if xx == B:
        res = x
        break
    else:
        x += 1

print(res)

