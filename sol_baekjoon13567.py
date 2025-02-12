import sys
# 1. 문제의 input을 받습니다.
m , n = map(int, sys.stdin.readline().split())

# 2. 현재 방향, 이동할 방향 배열, 현재 위치, 유효 여부 등 필요한 변수를 설정합니다.
dir = 0 # 동쪽 바라보고 시작
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1] #동, 남, 서, 북
x = 0
y = 0

flag = True

# 3. N개의 명령어에 대해 시뮬레이션 합니다.
for i in range(n):
    type, count = sys.stdin.readline().split()
    # 3-1. TURN일 경우 방향 이동합니다.
    if type == "TURN":
        if int(count) == 0:
            dir -= 1
        else:
            dir += 1
        dir %= 4
    # 3-2. MOVE일 경우 로봇을 이동시킵니다.
    elif type == "MOVE":
        x += dx[dir] * int(count)
        y += dy[dir] * int(count)
    # 3-3. 영역을 벗어나지 않았는지 판단합니다.
    if x < 0 or x > m or y < 0 or y > m:
        flag = False
        break

if flag:
    print(x,y)
else:
    print(-1)