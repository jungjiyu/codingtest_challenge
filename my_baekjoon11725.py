import sys
from collections import deque


def main():
    input = sys.stdin.readline
    N = int(input())

    # 인접 리스트 초기화
    adj = [[] for _ in range(N + 1)]

    for _ in range(N - 1):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # 부모를 저장할 배열, 0으로 초기화
    parent = [0] * (N + 1)

    # BFS를 위한 큐 초기화
    q = deque()
    q.append(1)  # 루트 노드 1부터 시작
    parent[1] = -1  # 루트 노드의 부모는 없음 (-1로 표시)

    while q:
        current = q.popleft()
        for neighbor in adj[current]:
            if parent[neighbor] == 0:
                parent[neighbor] = current
                q.append(neighbor)

    # 2번 노드부터 출력
    for i in range(2, N + 1):
        print(parent[i])


if __name__ == "__main__":
    main()
