import heapq
import sys

# 1. 문제의 input을 받습니다.
N, M, K, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append((y, 1)) # x 에서 y 방향의, 가중치가 1 인 간선
print(f"graph: {graph}")

# 2. 다익스트라 계산을 위한 초기 값을 설정합니다.
res = [int(1e9) for _ in range(N + 1)] # 모든 노드에 대한 대상 정점 까지의 최소거리
print(f"int(1e9): {int(1e9)}")


# 3. 다익스트라를 구현합니다.
def dijkstra(x):
    que = []
    heapq.heappush(que, (0, x))  # 초기 노드와 거리를 heap에 삽입합니다.
    print(f"que:{que}")
    res[x] = 0
    while que:
        dist, now = heapq.heappop(que)  # heap에서 가장 앞(최단거리)의 노드를 꺼냅니다.
        print(f"que:{que}, dist:{dist}, now:{now}")
        print(f"res[now]:{res[now]}")

        # dist : 현재 노드까지의 거리, now : 현재 탐색할 노드
        if res[now] < dist:  # 기록된 최단거리가 현재 노드까지의 거리보다 짧다면 더 탐색할 필요가 없습니다.
            print(f" continue")
            continue

        print(f"graph[now]:{graph[now]} ")
        for j in graph[now]:  # 탐색할 노드와 연결된 노드를 탐색합니다.
            # graph[시작정점] == { [도착정점1, 가중치] , [도착정점2, 가중치], ...  } , j[0] == 도착 정점, j[1] == 가중치
            cost = dist + j[1]  # 현재까지 거리 + 가중치를 더해 다음 정점까지의 거리를 계산합니다.
            print(f"j:{j}, cost : {cost}, res[j[0]]:{ res[j[0]]}")
            if cost < res[j[0]]:  # 거리가 기록된 최단 거리보다 짧다면 업데이트하고, heap에 삽입합니다.
                res[j[0]] = cost
                heapq.heappush(que, (cost, j[0]))
                print(f"heap updated: {que}")


# 4. 다익스트라 결과를 토대로 최단거리가 K인 도시를 선별합니다.
dijkstra(X)

ans = []
for i in range(1, N + 1):
    if res[i] == K:
        ans.append(i)

if len(ans) == 0:
    print('-1')
else:
    for x in ans:
        print(x)
