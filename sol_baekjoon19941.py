# import sys
# # 1. 문제의 input을 받습니다.
# N, K = map(int, sys.stdin.readline().split())
# str1 = list(sys.stdin.readline().strip())
#
# ans = 0
# for i in range(0, N):
#     # 2. 사람이 발견되면 인접한 K개의 원소를 탐색합니다.
#     if str1[i] == 'P':
#         for j in range(i-K, i+K+1):
#             # 3. 햄버거가 발견되면 바로 정답으로 사용하고 , 해당위치에서 탐색을 종료합니다.
#             if 0 <= j < N and str1[j] == 'H':
#                 str1[j] = 'X'
#                 ans += 1
#                 print(f"updated str1 : {str1}")
#                 break
# print(ans)



# 우축 우선으로 한다면?
import sys

# 1. 문제의 input을 받습니다.
N, K = map(int, sys.stdin.readline().split())
str1 = list(sys.stdin.readline().strip())

ans = 0
for i in reversed(range(0, N)):
    # 2. 사람이 발견되면 인접한 K개의 원소를 탐색합니다.
    if str1[i] == 'P':
        for j in reversed(range(max(0, i - K), min(N, i + K + 1))):
            # 3. 햄버거가 발견되면 바로 정답으로 사용하고 , 해당위치에서 탐색을 종료합니다.
            if str1[j] == 'H':
                str1[i] = 'X-P'
                str1[j] = 'X-H'
                ans += 1
                print(f"updated str1 : {str1}")
                break
print(ans)