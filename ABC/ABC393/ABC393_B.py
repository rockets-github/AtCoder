S = input()

ans = 0
for i in range(len(S)):
    if S[i] == 'A':
        for j in range(i + 1, len(S)):
            if j + (j - i) < len(S) and S[j] == 'B' and S[j + (j - i)] == 'C':
                ans += 1

print(ans)