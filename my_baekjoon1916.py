import heapq
from sys import stdin, stdout

input = stdin.readline
print = stdout.write

# 1. 문제의 input을 받기
N = int(input())
M = int(input())
# print(f"N:{N}, M:{M}\n")

# 2. graph 정보 저장하기
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y ,c= map(int, input().split())
    graph[x].append((y, c)) # x 에서 y 방향의, 가중치가 c 인 간선
# print(f"graph: {graph}\n")
start , end = map(int, input().split())
# print(f"start: {start},end:{end}\n")

res = [int(1e9) for _ in range(N + 1)] # 모든 노드에 대한 대상 정점 까지의 최소거리
# print(f"int(1e9): {int(1e9)}\n")

# 3. 다익스트라로 최소 경로 얻기
def dijkstra(x):
    que = []
    heapq.heappush(que, (0, x))  # 초기 노드와 거리를 heap에 삽입
    # print(f"que:{que}\n")

    res[x] = 0
    while que:
        dist, now = heapq.heappop(que)  # heap에서 가장 앞(최단거리)의 노드를 꺼냅니다.
        # print(f"que:{que}, res:{res}, dist:{dist}, now:{now}\n")
        # print(f"res[now]:{res[now]}\n")

        # dist : 현재 노드까지의 거리, now : 현재 탐색할 노드
        if res[now] < dist:  # 기록된 최단거리가 현재 노드까지의 거리보다 짧다면 더 탐색할 필요가 없습니다.
            # print(f" continue\n")
            continue

        # print(f"graph[now]:{graph[now]}\n")
        for j in graph[now]:  # 탐색할 노드와 연결된 노드를 탐색합니다.
            cost = dist + j[1]  # 현재까지 거리 + 가중치를 더해 다음 정점까지의 거리를 계산합니다.
            # print(f"j:{j}, cost : {cost}, res[{j[0]}]:{ res[j[0]]}")
            if cost < res[j[0]]:  # 거리가 기록된 최단 거리보다 짧다면 업데이트하고, heap에 삽입합니다.
                res[j[0]] = cost
                heapq.heappush(que, (cost, j[0]))
                # print(f"heap updated: {que}\n")


dijkstra(start)

# 4. 결과 출력하기
print(f"{res[end]}\n")