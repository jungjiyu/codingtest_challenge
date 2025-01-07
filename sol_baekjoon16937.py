import sys


# 3. 스티커 2종을 가로,세로로 붙일 때 모눈종이에 붙일 수 있는지 판단하는 코드를 구현합니다.
def check_available(r1, r2, c1, c2):
    # 스티커를 세로로 붙인 경우
    if (c1 + c2) <= H and max(r1, r2) <= W:
        return True
    # 스티커를 가로로 붙인 경우

# 1. 문제의 input을 받습니다.
H, W = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())
stickers = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

ans = 0
# 2. 스티커 중 2가지를 고르는 모든 경우의 수를 탐색합니다.
for i in range(N):
    for j in range(i + 1, N):
        # 4. 각 스티커에 2종에 대해 모눈종이에 붙일 수 있는지 판단하고, 정답을 업데이트 합니다.
        # 모두 회전하지 않은 경우
        if check_available(stickers[i][0], stickers[j][0], stickers[i][1], stickers[j][1]):
            ans = max(ans, stickers[i][0] * stickers[i][1] + stickers[j][0] * stickers[j][1])
        # 첫 스티커만 90도 회전할 경우
        if check_available(stickers[i][1], stickers[j][0], stickers[i][0], stickers[j][1]):
            ans = max(ans, stickers[i][0] * stickers[i][1] + stickers[j][0] * stickers[j][1])
        # 두번쨰 스티커만 90도 회전할 경우
        if check_available(stickers[i][0], stickers[j][1], stickers[i][1], stickers[j][0]):
            ans = max(ans, stickers[i][0] * stickers[i][1] + stickers[j][0] * stickers[j][1])
        # 두개 모두 90도 회전할 경우
        if check_available(stickers[i][1], stickers[j][1], stickers[i][0], stickers[j][0]):
            ans = max(ans, stickers[i][0] * stickers[i][1] + stickers[j][0] * stickers[j][1])

print(ans)
