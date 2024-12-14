def solve(N, S, A):
    total_sum = sum(A)
    S %= total_sum

    A.extend(A)

    prefix_sum = {0}
    current_sum = 0

    for a in A:
        current_sum += a
        prefix_sum.add(current_sum)

    for p in prefix_sum:
        if (p + S) in prefix_sum:
            return "Yes"

    return "No"


N, S = map(int, input().split())
A = list(map(int, input().split()))

print(solve(N, S, A))
