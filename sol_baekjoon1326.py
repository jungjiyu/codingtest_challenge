import sys
from collections import deque

# 1. 문제의 input을 받습니다.
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
a, b = map(int, sys.stdin.readline().split())

# 2. BFS 탐색을 위해 방문 체크를 위한 배열을 초기화 합니다 (-1)
visited = [-1 for _ in range(N)]

# 3. BFS 탐색을 구현합니다.
def bfs():
    # 3-1. 초기 시작 노드를 방문 체크한 후 queue에 넣습니다.
    que = deque([a-1])
    visited[a-1] = 0
    while que:
        # 3-2. queue의 맨 앞 노드를 탐색합니다.
        now = que.popleft()
        # 3-3. 오른쪽으로 이동할 수 있는 노드를 탐색하며, 방문하지 않았을 경우 최단거리 +1을 하고 queue에 넣습니다.
        for i in range(now, N, arr[now]):
            if visited[i] == -1:
                que.append(i)
                visited[i] = visited[now] + 1
                if i == b-1: # 최종 목적지에 도달하면 값을 리턴합니다.
                    return visited[i]
        # 3-4. 왼쪽으로 이동할 수 있는 노드를 탐색하며, 방문하지 않았을 경우 최단거리 +1을 하고 queue에 넣습니다.
        for i in range(now, -1, -arr[now]):
            if visited[i] == -1:
                que.append(i)
                visited[i] = visited[now] + 1
                if i == b-1: # 최종 목적지에 도달하면 값을 리턴합니다.
                    return visited[i]
    return -1

print(bfs())