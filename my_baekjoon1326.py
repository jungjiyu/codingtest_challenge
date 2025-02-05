from sys import stdin, stdout
from collections import deque

input = stdin.readline
print = stdout.write

def bfs(a, b, nodeValues):
    N = len(nodeValues) - 1
    queue = deque([a])
    visited = [False] * (N + 1)
    visited[a] = True
    count = 0

    while queue:
        size = len(queue)  # 현재 레벨의 노드 개수
        for _ in range(size):  # 현재 레벨의 모든 노드 탐색
            curNode = queue.popleft()

            if curNode == b:  # 목표 지점 도달
                return count

            step = nodeValues[curNode]
            for direction in [-1, 1]:  # 좌우 이동
                nextNode = curNode + direction * step
                while 1 <= nextNode <= N:  # 가능한 모든 점프 탐색
                    if not visited[nextNode]:
                        visited[nextNode] = True
                        queue.append(nextNode)
                    nextNode += direction * step  # 같은 배수로 계속 탐색

        count += 1  # 한 번의 점프 완료 후 증가

    return -1  # 목표 지점 도달 불가능

def main():
    N = int(input())
    nodeValues = list(map(int, input().split()))
    nodeValues.insert(0, 0)  # 인덱스 맞추기
    a, b = map(int, input().split())

    result = bfs(a, b, nodeValues)
    print(f"{result}\n")

if __name__ == "__main__":
    main()
