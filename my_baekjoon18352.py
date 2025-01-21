from collections import deque
from sys import stdin,stdout
input = stdin.readline
print=stdout.write
#1.input받기
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
#print(f"graph:{graph}, distance:{distance}, visited:{visited} \n")

#2. BFS 로 인근 노드 방문하면서 해당 노드에 대한 최단 거리 구하기
def bfs(start):
    answer = []
    q = deque([start])
    visited[start] = True
    distance[start] = 0
#    print(f"q:{q}, distance:{distance}, visited:{visited},answer:{answer}\n")
    while q:
        now = q.popleft()
        for i in graph[now]:
#            print(f"q:{q}, now:{now}, i : {i} \n")
            if not visited[i]:
                visited[i] = True
                q.append(i)
                distance[i] = distance[now] + 1
#                print(f"visited updated - visited :{visited}, q:{q}, distance : {distance} \n")
                if distance[i] == k:
                    answer.append(i)
#                    print(f"answer updated : {answer}\n")
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(f"{i}\n")

bfs(x)