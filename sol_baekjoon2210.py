import sys

board = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 문제의 input을 받습니다.
for _ in range(5):
    arr = sys.stdin.readline().split()
    board.append(arr)


s1 = set()

# 2. 각 위치에서의 5번 이동하는 탐색을 구현합니다.
def dfs(x, y, now):
    now += str(board[x][y]) # 2-1. 현재 숫자를 string에 이어붙입니다.
    if len(now) == 6: #2-2. 길이가 6이라면 set에 추가하고 탈출합니다.
        s1.add(now)
        return

    for i in range(4): # 2-3. 상,하,좌,우로 탐색을 이어 진행합니다.
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= 5 or ny < 0 or ny >=5:
            continue
        dfs(nx,ny,now)

# 3. 숫자판 위의 모든 위치에서 탐색을 진행합니다.
for i in range(5):
    for j in range(5):
        dfs(i,j,"")

print(len(s1))