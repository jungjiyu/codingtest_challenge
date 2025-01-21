import heapq
import sys
# 1. 문제의 input을 받습니다.
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x, y, cost = map(int, sys.stdin.readline().split())
    graph[x].append((y, cost))
A, B = map(int,sys.stdin.readline().split())

# 2. 다익스트라 계산을 위한 거리 초기 값을 설정합니다.
distance = [int(1e9) for _ in range(N+1)]

# 3. 다익스트라를 구현합니다.
def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for j in graph[now]:
            weight = j[1]
            next_node = j[0]
            cost = dist + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(que, (cost, next_node))

# 4. 도시 A에서 다익스트라 탐색을 진행합니다.
dijkstra(A)
print(distance[B])
