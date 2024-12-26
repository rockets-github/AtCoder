N = list(bin(int(input())))
ctz = 0
for i in reversed(N):
    if int(i) == 0:
        ctz += 1
    else:
        break

print(ctz)