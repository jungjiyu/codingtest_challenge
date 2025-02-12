import sys
# 1. 문제의 input을 받습니다.
n = int(sys.stdin.readline())
arr =[]
for _ in range(n):
    arr.append(list(map(int, sys.stdin.readline().split())))

# 2. dp 탐색을 위한 초기 값을 설정합니다.
dp = [[0 for _ in range(3)]for _ in range(n)]
dp[0] = arr[0]

# 3. N번째 집 까지 DP 탐색을 진행합니다.
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + arr[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + arr[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + arr[i][2]

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))