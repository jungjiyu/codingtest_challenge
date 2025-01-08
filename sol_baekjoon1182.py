import sys
sys.setrecursionlimit(10**6)

# 1. 문제의 input을 받습니다.
N , S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

ans = 0

# 2. 모든 부분 수열을 탐색하는 과정을 구현합니다.
def dfs(idx, total):
    global ans
    if idx == N: # 2- 3. idx N까지 도달했을 경우, 모든 선택을 맞췄기 때문에 정답을 만족하는지 확인
        if total == S:
            ans += 1
        return
    dfs(idx+1, total) # 2- 1. 해당 idx를 선택하지 않는 경우, 총 합에 추가하지 않음
    dfs(idx+1, total + arr[idx]) # 2- 2. 해당 idx를 선택하는 경우, 총 합에 추가

# 3. 탐색을 진행하고 정답을 출력합니다.
dfs(0, 0)
if S == 0:
    ans -= 1
print(ans)