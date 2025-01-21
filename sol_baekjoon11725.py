import sys

# 1. 문제의 input을 받고 그래프를 저장합니다.
from collections import deque
N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    x, y = map(int, sys.stdin.readline().split())
    arr[x].append(y)
    arr[y].append(x)

# 2. bfs 탐색을 위한 queue를 만들고, 초기 값을 설정합니다.
now = 1
que = deque()
que.append(1)

parent = [0 for _ in range(N+1)]
parent[1] = 1

# 3. bfs 탐색을 진행합니다. 방문 여부는 부모 노드가 설정 되었는지 여부로 한번에 체크합니다.
while que:
    now = que.popleft()
    for x in arr[now]:
        if parent[x] == 0:
            parent[x] = now
            que.append(x)

for i in range(2, N+1):
    print(parent[i])
