import sys

# 1. DP 탐색을 위한 초기 값을 설정합니다.
DP = [0 for _ in range(11)]
DP[1] = 1
DP[2] = 2
DP[3] = 4

# 2. 세운 점화식에 맞게 DP 탐색을 진행합니다.
for i in range(4, 11):
    DP[i] = DP[i-3] + DP[i-2] + DP[i-1]

# 3. 문제의 input을 받고, 구해놓은 DP 값에 맞게 답을 출력합니다.
T = int(sys.stdin.readline())
for _ in range(T):
    print(DP[int(sys.stdin.readline())])