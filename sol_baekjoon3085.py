import sys

# 1. 문제의 input을 받습니다.
n = int(sys.stdin.readline())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

# 2. 가장 긴 연속된 부분을 구하는 함수를 구현합니다.
def calc_max_candy():
    res = 0
    for i in range(n):
        # 가로 최대 개수 확인
        now = 1
        for j in range(1, n):
            if board[i][j] == board[i][j - 1]:
                now += 1
            else:
                now = 1
            res = max(now, res)

        # 세로 최대 개수 확인
        now = 1
        for j in range(1, n):
            if board[j][i] == board[j - 1][i]:
                now += 1
            else:
                now = 1
            res = max(now, res)
    return res

# 3. 모든 경우를 탐색합니다.
ans = 0
for i in range(n):
    for j in range(n):
        # 3-1. 오른쪽 스왑
        if j+1 < n and board[i][j] != board[i][j+1]:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, calc_max_candy())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        # 3-2. 아래로 swap
        if i+1 < n and board[i][j] != board[i+1][j]:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, calc_max_candy())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)