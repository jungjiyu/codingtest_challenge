import sys

# 1. 문제의 input을 받습니다.
R, C = map(int, sys.stdin.readline().split())
board = []

for _ in range(R):
    board.append(list(sys.stdin.readline().strip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2. 인접한 바다의 개수를 구하는 코드를 구현합니다.
def check_sea(x, y):
    count = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            count += 1
        else:
            if board[nx][ny] == '.':
                count += 1
    return count


# 3. 섬의 위치마다 인접한 바다의 개수를 구하고, 잠긴 곳으로 표기합니다.
sink = []

for i in range(R):
    for j in range(C):
        if board[i][j] == 'X':
            if check_sea(i, j) >= 3:
                sink.append((i, j))

# 4. 잠긴 곳의 정보를 토대로 지도를 업데이트 합니다.
for x, y in sink:
    board[x][y] = '.'

# 5. 출력해야 할 지도의 최소 크기를 구합니다.
minX = R
maxX = 0
minY = C
maxY = 0

for x in range(R):
    for y in range(C):
        if board[x][y] == 'X':
            minX = min(minX, x)
            maxX = max(maxX, x)
            minY = min(minY, y)
            maxY = max(maxY, y)

# 6. 최소 크기에 맞게 지도를 출력합니다.
for i in range(minX, maxX + 1):
    for j in range(minY, maxY + 1):
        print(board[i][j], end='')
    print()
