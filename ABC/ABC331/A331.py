m, d = map(int,input().split())
year, month, day = map(int,input().split())

if day == d:
    day = 1
    if month == m:
        month = 1
        year += 1
    else:
        month += 1
else:
    day += 1

print(year, month, day)
