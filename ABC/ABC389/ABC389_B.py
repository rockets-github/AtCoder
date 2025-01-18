import math

X = int(input())

for i in range(1, 21):
    if math.factorial(i) == X:
        print(i)
