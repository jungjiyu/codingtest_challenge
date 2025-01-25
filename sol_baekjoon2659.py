import sys

# 1. 문제의 input을 받습니다.(이어 붙인 형태로 변환해둡니다)
input_number = ''.join(sys.stdin.readline().split())

# 2. 시계수를 계산하는 함수를 구현합니다.
def make_clock_number(number):
    res = 9999
    arr = list(map(int, str(number)))
    for i in range(4):
        now = int(arr[(i + 1) % 4] * 1000 + arr[(i + 2) % 4] * 100 + arr[(i + 3) % 4] * 10 + arr[(i + 4) % 4])
        if res > now:
            res = now
    return res

# 3. 0이 포함되어 있는지 확인하는 함수를 구현합니다.
def include_zero(number):
    arr = list(map(int, str(number)))
    if 0 in arr:
        return True
    else:
        return False

# 4. 현재 input의 시계수를 구합니다.
input_clock_number = make_clock_number(input_number)
ans = 1

# 5. 가장 작은 수 부터 시계 수까지 탐색합니다.
for i in range(1111, input_clock_number):
    if not include_zero(i): # 6. 현재 수가 0으로 포함하지 않는지 확인합니다.
        now_clock_number = make_clock_number(i) # 7. 현재 수가 시계수가 맞는지 확인합니다.
        if now_clock_number == i: # 8. 맞다면 개수를 + 1 합니다.
            ans += 1
print(ans)
