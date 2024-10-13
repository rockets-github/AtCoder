N = int(input())
b_ate = ""
for i in range(N - 1):
    ate = input()
    if b_ate == ate == "sweet":
        print("No")
        exit()
    else:
        b_ate = ate
print("Yes")
exit()
