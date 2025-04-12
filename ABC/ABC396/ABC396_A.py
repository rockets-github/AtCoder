N = int(input())
A = list(map(int, input().split()))

ct = 0
before = 101

for i in A:
    if before == i:
        ct += 1
        if ct == 3:
            print("Yes")
            exit()
    else:
        ct = 1
    before = i


print("No")
