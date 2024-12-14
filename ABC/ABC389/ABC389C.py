a, b, c, d, e = map(int, input().split())
score_dict = {"A": a, "B": b, "C": c, "D": d, "E": e}


chars = "ABCDE"
n = len(chars)
result = {}
for i in range(1, 1 << n):
    subset = []
    score = 0
    for j in range(n):
        if i & (1 << j):
            subset.append(chars[j])
    for j in subset:
        score += score_dict[j]
    result["".join(subset)] = score


result = sorted(result.items(), key=lambda x: (-x[-1], x[0]))
for res in result:
    print(res[0])
