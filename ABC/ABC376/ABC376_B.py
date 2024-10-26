N, Q = map(int, input().split())

handL = 1
handR = 2

mc = 0


def count_move(now_hand, check_hand, mt):
    min_p, max_p = min(now_hand, mt), max(now_hand, mt)

    if min_p < check_hand < max_p:
        return (N - max_p) + min_p
    else:
        return max_p - min_p


for _ in range(Q):
    hand, mt = input().split()
    mt = int(mt)

    if hand == "L":
        mc += count_move(handL, handR, mt)
        handL = mt
    else:
        mc += count_move(handR, handL, mt)
        handR = mt

print(mc)