import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 1. 문제의 Input을 받습니다.
r, c = map(int, sys.stdin.readline().split())
visited = [[False for _ in range(c)] for _ in range(r)]

k = int(sys.stdin.readline())
for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    visited[x][y] = True

x, y = map(int, sys.stdin.readline().split())
visited[x][y] = True
order = list(map(int, sys.stdin.readline().split()))

# 2. index 활용을 위해 입력 받은 order 배열의 값을 조정합니다.
for i in range(len(order)):
    order[i] -= 1

dir = 0
while True:
    moved = False
    for i in range(4): # 3. 현재방향 부터 4방향 탐색을 진행합니다.
        # 4. 탐색 중인 방향에 맞게 다음 위치를 지정합니다.
        now_dir = (dir + i) % 4
        nx = x + dx[order[now_dir]]
        ny = y + dy[order[now_dir]]
        # 5. 다음 위치가 방문가능한 곳인지 판단합니다.
        if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
            # 6. 방문 가능한 곳이라면 위치와 방향을 업데이트 합니다.
            x = nx
            y = ny
            dir = now_dir
            visited[x][y] = True
            # 7. 이동 가능했다는 표기를 합니다.
            moved = True
            break
    # 8. 이동하지 못했다면 탐색을 종료합니다.
    if not moved:
        break
print(x,y)
