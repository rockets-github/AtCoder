# from pprint import pprint


# def check_mate(chess_board, y, x, C):
#     x -= 1
#     y -= 1

#     chess_board[y][x] = False
#     # ２列下
#     if y <= C - 2:
#         # 右
#         if x <= C - 1:
#             chess_board[y + 2][x + 1] = False
#         # 左
#         if 1 <= x:
#             chess_board[y + 2][x - 1] = False

#     # 1列下
#     if y <= C - 1:
#         # 右
#         if x <= C - 2:
#             chess_board[y + 1][x + 2] = False
#         # 左
#         if 2 <= x:
#             chess_board[y + 1][x - 2] = False

#     # ２列上
#     if y >= 2:
#         # 右
#         if x <= C - 1:
#             chess_board[y - 2][x + 1] = False
#         # 左
#         if 1 <= x:
#             chess_board[y - 2][x - 1] = False

#     # 1列上
#     if y >= 1:
#         # 右
#         if x <= C - 2:
#             chess_board[y - 1][x + 2] = False
#         # 左
#         if 2 <= x:
#             chess_board[y - 1][x - 2] = False

#     return chess_board


# N, M = map(int, input().split())
# chess_board = [[True] * N for i in range(N)]
# for i in range(M):
#     y, x = map(int, input().split())
#     chess_board = check_mate(chess_board, y, x, N - 1)


# print(sum(map(sum, chess_board)))

def check_mate(occupied_cells, y, x, N):
    moves = [
        (2, 1), (2, -1), (1, 2), (1, -2),
        (-2, 1), (-2, -1), (-1, 2), (-1, -2)
    ]


    for dy, dx in moves:
        ny, nx = y + dy, x + dx

        if 0 <= ny < N and 0 <= nx < N:
            occupied_cells.add((ny, nx))

N, M = map(int, input().split())
occupied_cells = set()
for _ in range(M):
    y, x = map(int, input().split())
    check_mate(occupied_cells, y - 1, x - 1, N)


result = N * N - len(occupied_cells)
print(result)
