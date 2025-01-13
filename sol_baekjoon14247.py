import sys
# 1. 문제의 input을 받습니다.
N = int(sys.stdin.readline())

init_height = list(map(int, sys.stdin.readline().split()))
growth = list(map(int, sys.stdin.readline().split()))

# 2. 나무를 성장 길이에 따라 정렬합니다.
arr = []
for i in range(N):
    arr.append([growth[i], init_height[i]])
arr.sort()

# 3. n일차까지 순회하며 획득한 나무의 양을 더해줍니다.
ans = 0
for i in range(N):
    ans += arr[i][0] * i + arr[i][1]

print(ans)