import sys
# 1. 문제의 input을 받습니다.
C, R = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

# 2. 문제의 조건에 맞게 방향 전환 순서를 정의합니다.
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 3. 시뮬레이션을 위한 초기 값을 설정합니다.
visited = [[False for _ in range(R+1)] for _ in range(C+1)]
x = 1
y = 1
dir = 0
visited[1][1] = True

# 4. 탐색을 시작하기 전 , 좌석 배정이 불가능한 경우에 대한 예외처리를 진행합니다.
if K > R * C:
    print('0')
else: # 5. 자리 배치 시뮬레이션을 진행합니다.
    for i in range(1, K):
        # 5-1. 현재 방향에서 다음 자리를 확인합니다.
        nx = x + dx[dir]
        ny = y + dy[dir]
        # 5-2. 다음 자리가 배치 가능한 곳인지 확인합니다.(공연장 밖이거나 이미 자리가 채워진 곳이면 방향 전환)
        if nx <= 0 or nx > C or ny <= 0 or ny > R or visited[nx][ny]:
            # 5-3. 배치 불가능한 곳이라면, 방향을 다음 방향으로 전환하고 다시 다음 자리를 구합니다.
            dir = (dir+1) % 4
            nx = x + dx[dir]
            ny = y + dy[dir]
        # 5-4. 자리를 업데이트하고 방문 체크를 합니다.
        x = nx
        y = ny
        visited[x][y] = True
    print(x, end = ' ')
    print(y)

