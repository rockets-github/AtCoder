h, w = map(int, input().split())

A = [input() for _ in range(h)]
B = [input() for _ in range(h)]


for i in range(h):
    A = A[1:] + A[:1]
    for i in range(w):
        for j in range(h):
            A[j] = A[j][1:] + A[j][:1]
        if A == B:
            print('Yes')
            exit()

print('No')

