import sys
import heapq

# 1. 문제 input을 받습니다.
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# 2. 사진틀을 관리하기 위한 dict를 생성합니다. key - 학생 번호, value - 추천 수
candidate_heap = {}

for x in arr:
    # 3. 후보가 사진틀 안에 존재할 경우 추천수(value)를 +1 합니다.
    if x in candidate_heap:
        candidate_heap[x] += 1
    else:
        # 4. 사진틀 개수가 N개 이상일 경우, 조건을 만족하는 삭제 대상 학생 번호를 찾습니다.
        if len(candidate_heap) >= N:
            del_key = heapq.nsmallest(1, candidate_heap, key=candidate_heap.get)
            # 5. 조건을 만족하는 학생 번호를 사진틀에서 삭제합니다.
            candidate_heap.pop(del_key[0])
        # 6. 새로운 후보를 등록합니다.
        candidate_heap[x] = 1

# 7. 정답 출력을 위해 학생 번호 오름차순으로 정렬합니다.
res = sorted(candidate_heap.keys())
for i in res:
    print(i, end=' ')