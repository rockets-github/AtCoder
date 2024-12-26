from collections import defaultdict
countDict = defaultdict(int)
N, M = map(int,input().split())
vote = list(map(int, input().split()))

max_vote = 0
voted = 0
for i in vote:
    if i in countDict.keys():
        countDict[i] += 1
    else:
        countDict[i] = 1

    if countDict[i] > max_vote:
        max_vote = countDict[i]
        voted = i
    elif countDict[i] == max_vote:
        voted = min(voted, i)
    else:
        pass

    print(voted)
