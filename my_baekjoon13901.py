from sys import stdin,stdout

input = stdin.readline
print = stdout.write

# 방향 정의 (상, 하, 좌, 우)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move_robot(R, C, startY, startX, direction_order, obstacles):
    visited = [[False] * C for _ in range(R)]
    visited[startY][startX] = True  # 시작 위치 방문 처리

    # 로봇 현재 위치
    curY, curX = startY, startX

    while True:
        moved = False  # 이동 여부 확인

        for d in direction_order:
            nextY, nextX = curY + dy[d - 1], curX + dx[d - 1]

            # 해당 방향으로 이동 가능한지 확인
            while 0 <= nextX < C and 0 <= nextY < R and not visited[nextY][nextX] and (nextY, nextX) not in obstacles:
                curY, curX = nextY, nextX
                visited[curY][curX] = True
                nextY += dy[d - 1]
                nextX += dx[d - 1]
                moved = True

            # 더 이상 이동할 수 없으면 반복문 탈출 후 다음 방향 확인

        # 어떤 방향으로도 이동하지 못했다면 종료
        if not moved:
            return curY, curX


def main():
    R, C = map(int, input().split())
    K = int(input())
    obstacles = set(tuple(map(int, input().split())) for _ in range(K))
    sr, sc = map(int, input().split())
    direction_order = list(map(int, input().split()))
    #print(f"R,C:{R},{C}\nobstacles:{obstacles}\nsr,sc:{sr},{sc}\ndirection_order:{direction_order}\n")

    # 로봇의 최종 위치 계산
    final_y, final_x = move_robot(R, C, sr, sc, direction_order, obstacles)
    print(f"{final_y} {final_x}")

if __name__ == "__main__":
    main()
