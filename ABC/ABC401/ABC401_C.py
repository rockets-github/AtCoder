def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    K = int(data[1])
    S = data[2]

    # 前からのDP
    dp_forward = [[False] * 2 for _ in range(K+1)]
    dp_forward[0][0] = True  # 0個のo、最後が.

    for i in range(N):
        new_dp = [[False] * 2 for _ in range(K+1)]
        c = S[i]
        for k in range(K+1):
            for last in range(2):  # 0: ., 1: o
                if not dp_forward[k][last]:
                    continue
                if c == '.' or c == '?':
                    new_dp[k][0] = True
                if (c == 'o' or c == '?') and k < K and last != 1:
                    new_dp[k+1][1] = True
        dp_forward = new_dp

    # 後ろからのDP
    dp_backward = [[False] * 2 for _ in range(K+1)]
    dp_backward[0][0] = True  # 0個のo、最後が.

    for i in range(N-1, -1, -1):
        new_dp = [[False] * 2 for _ in range(K+1)]
        c = S[i]
        for k in range(K+1):
            for last in range(2):  # 0: ., 1: o
                if not dp_backward[k][last]:
                    continue
                if c == '.' or c == '?':
                    new_dp[k][0] = True
                if (c == 'o' or c == '?') and k < K and last != 1:
                    new_dp[k+1][1] = True
        dp_backward = new_dp

    # 各位置の可能性を判定
    result = []
    for i in range(N):
        can_dot = False
        can_o = False
        c = S[i]
        
        # 前からのDPと後ろからのDPを組み合わせて判定
        for k1 in range(K+1):
            for last1 in range(2):
                if not dp_forward[k1][last1]:
                    continue
                for k2 in range(K+1):
                    if k1 + k2 > K:
                        continue
                    for last2 in range(2):
                        if not dp_backward[k2][last2]:
                            continue
                        if c == '.' or c == '?':
                            can_dot = True
                        if (c == 'o' or c == '?') and k1 + k2 < K and last1 != 1 and last2 != 1:
                            can_o = True

        if can_dot and can_o:
            result.append('?')
        elif can_dot:
            result.append('.')
        else:
            result.append('o')

    print(''.join(result))

if __name__ == "__main__":
    main()
