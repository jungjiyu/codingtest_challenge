import sys
# 1. 문제의 input을 받습니다.
N, A, B = map(int, sys.stdin.readline().split())
arr1 = list(map(int,sys.stdin.readline().split()))
arr2 = list(map(int,sys.stdin.readline().split()))

# 2. 각 타일을 크기가 큰 순서대로 정렬합니다.
arr1.sort(reverse=True)
arr2.sort(reverse=True)
ans, idx1, idx2 = 0, 0, 0

# 3. 홀수일 경우, 2x1 타일 중 가장 큰 값의 타일을 사용합니다.
if N %2 == 1:
    ans += arr1[0]
    arr1.pop(0)

# 4. 2x2 크기의 타일들을 만들어 채워나가며 탐색합니다.
for _ in range(N //2):
    case1, case2 = 0, 0
    if len(arr1) >= 2: # 4-1. 2X1 크기의 타일을 2개 사용 하는 경우
        case1 = arr1[0] + arr1[1]
    if len(arr2) >= 1: # 4-2. 2X2 크기의 타일을 1개 사용 하는 경우
        case2 = arr2[0]

    if case1 > case2:
        ans += case1
        arr1.pop(0)
        arr1.pop(0)
    else:
        ans += case2
        arr2.pop(0)
print(ans)

