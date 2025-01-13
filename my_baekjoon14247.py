# 1. input 값 받기
n = int(input())
H = list(map(int, input().split()))
A = list(map(int, input().split()))


utilList = []
for i in range(len(H)):
    utilList.append([H[i], A[i]])

utilList.sort(key=lambda x: x[1]) # 나무를 자라는 속도를 기준으로 오름차순 정렬

# 2. 최대 나무 길이의 나무 자르기
totalLength = 0
for i in range(len(utilList)):
    totalLength += i * utilList[i][1] + utilList[i][0]

# 3. 결과 출력
print(totalLength)