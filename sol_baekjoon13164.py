import sys

# 1. 문제의 input을 받습니다.
N, K = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 2. 인접한 키차이를 구하고, 이를 정렬합니다.
gaps = []
for i in range(1, N):
    gaps.append(arr[i]-arr[i-1])
gaps.sort()

# 3. 가장 큰 K-1개의 키 차이를 제외한 인접한 키차이의 합을 구합니다.
if K == 1:
    print(sum(gaps))
else:
    print(sum(gaps[:-(K-1)]))