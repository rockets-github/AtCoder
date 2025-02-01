N, M = map(int, input().split())
S = [list(input()) for _ in range(N)]
T = [list(input()) for _ in range(M)]


def check(a, b):
    for i in range(len(T)):
        for j in range(len(T)):
            if T[i][j] != S[i + a - 1][j + b - 1]:
                return False
    return True


diff = N - M + 1
for a in range(1, diff + 1):
    for b in range(1, diff + 1):
        is_ok = check(a, b)
        if is_ok:
            print(a, b)
            exit()
