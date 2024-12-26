from collections import defaultdict
countDict = defaultdict(int)
N = int(input())
S = list(input())

before_str = 'XXX'
ct = 0
for i in S:
    if i != before_str:
        ct = 1
        before_str = i
    else:
        ct += 1
    if i in countDict.keys():
        if countDict[i] < ct:
            countDict[i] = ct
    else:
        countDict[i] = ct

print(sum(countDict.values()))
