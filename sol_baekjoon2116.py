import sys

# 1. 문제의 input을 받습니다.
N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 2. 아래면 index를 기준으로 아래-위 숫자를 제외한 수들 중 최댓값을 찾는 함수를 구현합니다.
def find_max(arr, idx):
    res = 0
    if idx == 0 or idx == 5:
        res = max(arr[1], arr[2], arr[3], arr[4])
    elif idx == 1 or idx == 3:
        res = max(arr[0], arr[2], arr[4], arr[5])
    elif idx == 2 or idx == 4:
        res = max(arr[0], arr[1], arr[3], arr[5])
    return res

# 3. 아래면 index를 기준으로 윗면 숫자를 찾는 함수를 구현합니다.
def find_top(arr, bottom_idx):
    top = 0
    if bottom_idx == 0:
        top = arr[5]
    elif bottom_idx == 1:
        top = arr[3]
    elif bottom_idx == 2:
        top = arr[4]
    elif bottom_idx == 3:
        top = arr[1]
    elif bottom_idx == 4:
        top = arr[2]
    elif bottom_idx == 5:
        top = arr[0]
    return top

# 4. 1번 주사위의 6가지 수에 대해 주사위 쌓기를 시뮬레이션 합니다.
ans = 0
for i in range(6):
    top = arr[0][i] # 4-1. 1번 주사위의 윗면 숫자를 초기 top으로 설정합니다.
    total = find_max(arr[0], i) # 4-2. 1번 주사위에서 최대 숫자를 구해 합산합니다.
    for j in range(1, N):
        bottom_idx = arr[j].index(top) # 4-3. 전의 주사위의 top값과 일치하는 bottom값의 index를 구합니다.
        top = find_top(arr[j], bottom_idx) # 4-4. bottom 값의 index를 기준으로 top값을 찾습니다.
        total += find_max(arr[j], bottom_idx) # 4-5. 아래 위 값을 제외한 값들 중 최댓값을 구해 합산합니다.
    ans = max(ans, total) # 5. 정답과 비교해 현재 경우에서 구한 최댓값이 더 크면 정답을 업데이트 합니다.
print(ans)
