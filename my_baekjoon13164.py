from sys import stdin, stdout
import math

input = stdin.readline
print = stdout.write


# 1. input 입력받기
N,K = map(int,input().split())
children = list(map(int,input().split()))
#print(f"N:{N}, K:{K}, children:{children}\n")

# 2. 인접 차이 내림차순 정렬
adjacentDiff = []
for i in range(N-1):
    adjacentDiff.append(children[i+1]-children[i])

adjacentDiff.sort(reverse=True) # 내림차순 정렬
#print(f"adjacentDiff:{adjacentDiff}\n")

#3. 가장 큰 k-1 개 지점 무시
minSum = 0
if K == 1:
    minSum = children[-1] - children[0]
else:
    # 전체 구간 비용에서, 가장 큰 (K-1)개의 diff를 빼주면 된다
    minSum = (children[-1] - children[0]) - sum(adjacentDiff[:K-1])


# 4. 결과 출력
print(f"{minSum}\n")
