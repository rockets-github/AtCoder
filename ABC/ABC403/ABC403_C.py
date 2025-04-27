N, M, Q = map(int, input().split())

# ユーザーごとの閲覧権限を管理
user = [set() for _ in range(N)]
all_access = [False] * N  # 全ページ閲覧権限を持つかどうかのフラグ

# Qこのクエリを処理する
for _ in range(Q):
    query = list(map(int, input().split()))

    match query[0]:
        case 1:
            # ユーザーXにコンテストページYの閲覧権限を付与
            user[query[1] - 1].add(query[2] - 1)
        case 2:
            # ユーザーXに全てのコンテストページの閲覧権限を付与
            all_access[query[1] - 1] = True
        case 3:
            # ユーザーXがコンテストページYを閲覧できるか答える
            if all_access[query[1] - 1] or query[2] - 1 in user[query[1] - 1]:
                print("Yes")
            else:
                print("No")
