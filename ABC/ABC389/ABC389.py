r = int(input())

ans = 0
h = r + 1
for i in range(r + 1):
    while h > 0 and (h + 0.5) ** 2 + (i + 0.5) ** 2 > r**2:
        h -= 1
    ans += h

print(ans * 4 + 1)
