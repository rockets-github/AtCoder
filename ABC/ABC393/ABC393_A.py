S1, S2 = input().split()

if S1 == "sick" and S2 == "sick":
    print(1)

if S1 == "sick" and S2 == "fine":
    print(2)

if S1 == "fine" and S2 == "sick":
    print(3)

if S1 == "fine" and S2 == "fine":
    print(4)
