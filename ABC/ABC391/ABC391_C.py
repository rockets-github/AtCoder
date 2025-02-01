N, Q = map(int, input().split())
hat_pos = list(range(N))
su = [1] * N
m_su = 0
for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 2:
        print(m_su)
    else:

        # 移動前の数値
        hato_num = query[1] - 1
        ikisaki = query[2] - 1

        hato_now = hat_pos[hato_num]

        if su[hato_now] == 2:
            m_su -= 1

        if su[ikisaki] == 1:
            m_su += 1

        su[hato_now] -= 1
        su[ikisaki] += 1

        hat_pos[hato_num] = ikisaki
