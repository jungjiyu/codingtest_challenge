import sys

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

# 2. 섬을 탐색하는 BFS를 구현합니다.
def bfs(x, y):
    queue = [(x, y)]
    global graph
    graph[x][y] = 0

    while queue:
        x, y = queue.pop()
        for i in range(8):
            # 2-1. 상하좌우 대각선으로 이어진 다음 노드를 구합니다.
            nx = x + dx[i]
            ny = y + dy[i]
            # 2-2. 지도 밖을 넘어가지 않았는지 확인합니다.
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            # 2-3. 방문한 곳은 아닌지, 바다는 아닌지 확인합니다.
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

while True:
    # 1. 문제의 input을 받습니다.
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    ans = 0
    for i in range(h):
        for j in range(w):
            # 3. 새로운 땅이 발견되었다면 , 정답을 +1 하고 인접한 땅을 탐색합니다.
            if graph[i][j] == 1:
                ans += 1
                bfs(i,j)
    print(ans)
