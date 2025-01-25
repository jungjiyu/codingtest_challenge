import sys
from collections import deque


def bfs(v):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    q = deque([v])
    #print(f"queue before while:{q}")

    while q:
        #print(f"1- cur queue: {q}")
        a, b = q.popleft()
        #print(f"2- cur a, b (queue popped): ({a},{b})")

        # 각 정점에 길의 개수
        cnt = 0

        # 상/하/좌/우 탐색
        for i in range(4):

            x = a + dx[i]
            y = b + dy[i]

            # 범위 내에 있고 길이라면
            if -1 < x < r and -1 < y < c and graph[x][y] == ".":

                # 4가지 방향에 길의 수 체크
                cnt += 1

                # 탐색하지 않았다면 탐색
                if visited[x][y] == False:
                    visited[x][y] = True

                    q.append([x, y])
                    #print(f"3- cur queue([{x},{y}]appended) : {q}")

        # 4가지 방향을 탐색했을 때 길이 2가지 미만이면 1을 리턴
        if cnt < 2:
            return 1

    # 모든 구역을 탐색했으면 0을 리턴
    return 0


r, c = map(int, sys.stdin.readline().split())
chek = [] # 길 좌표 확인

# 그래프를 표현
graph = []
for i in range(r):
    graph.append(list(map(str, sys.stdin.readline().strip())))
    for j in range(c):
        if graph[i][j] == ".":
            chek.append([i, j])
#print(f"chek:{chek}")
visited = [[False] * c for _ in range(r)]

# 모든 길이 연결되어 있음으로 하나의 길만을 탐색
print(bfs(chek[0]))