N = int(input())
res = 0
Takahashi = 0
Aoki = 0

for i in range(N):
    t, a = map(int, input().split())
    Takahashi += t
    Aoki += a

if Takahashi > Aoki:
    print('Takahashi')
elif Aoki > Takahashi:
    print('Aoki')
else:
    print('Draw')