S = list(input())
S.reverse()

for i in range(len(S) - 1):
    if S[i]+S[i+1] == 'AW':
        S[i] = "C"
        S[i+1] = "A"

S.reverse()

print("".join(S))


