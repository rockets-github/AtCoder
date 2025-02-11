A = list(map(int, input().split()))
sorted_A = sorted(A)

for i in range(len(A) - 1):
    check_A = A.copy()
    check_A[i], check_A[i + 1] = check_A[i + 1], check_A[i]
    if sorted_A == check_A:
        print("Yes")
        exit()

print("No")
