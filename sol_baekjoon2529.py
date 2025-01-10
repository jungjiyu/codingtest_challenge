import sys
from itertools import permutations

# 1. 문제의 input을 받습니다.
K = int(sys.stdin.readline())
arr = list(sys.stdin.readline().split())
numbers = [0,1,2,3,4,5,6,7,8,9]

# 2. K+1개의 원소를 선택하는 모든 순열을 구합니다.
nPr = list(permutations(numbers,K+1))


# 3. 해당 순열이 부등호를 만족시키는지 확인하는 함수를 구현합니다.
def check_ok(numbers):
    flag = True
    for i in range(0,K):
        if arr[i] == '<':
            if not numbers[i] < numbers[i+1]:
                flag = False
                break
        if arr[i] == '>':
            if not numbers[i] > numbers[i+1]:
                flag = False
                break
    return flag

# 4. 순열을 우선 거꾸로 탐색해 최댓값을 탐색합니다.
for x in reversed(nPr):
    if check_ok(x):
        for i in x:
            print(i,end='')
        break
print()

# 5. 순열을 순차적으로 탐색해 최솟값을 탐색합니다.
for x in nPr:
    if check_ok(x):
        for i in x:
            print(i, end='')
        break