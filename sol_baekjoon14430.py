import sys

# 1. 문제의 Input을 받습니다.
n, m = map(int, sys.stdin.readline().split())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

# 2. DP 탐색을 위한 초기화를 합니다.
DP =[[0 for _ in range(m)] for _ in range(n)]

# 3. 세운 점화식에 맞게 DP 탐색을 진행합니다.
for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            DP[i][j] = board[i][j]
        elif i == 0:
            DP[i][j] = DP[i][j-1] + board[i][j]
        elif j == 0:
            DP[i][j] = DP[i-1][j] + board[i][j]
        else:
            DP[i][j] = max(DP[i-1][j], DP[i][j-1]) + board[i][j]

# 4. 최종 위치에서의 값을 출력합니다.
print(DP[n-1][m-1])