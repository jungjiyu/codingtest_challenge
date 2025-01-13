from sys import stdin, stdout

input = stdin.readline
print = stdout.write

# 1. input 받기
N,K= map(int,input().split())
print(f"N:{N}, K:{K}\n")
tableList = list(input().strip())
print(f"tableList:{tableList}\n")



# 2. 각 P 에게 최적의 H 할당
count = 0
for i in range(N):
    if tableList[i] == 'P':  # 사람이 발견되면
        # 사람의 범위 내에 있는 햄버거 탐색
        # max(0, i - K) -> i-k 가 유효한 인덱스면 자동적으로 i-k 반환
        # min(N, i + K + 1) -> i+K+1 이 유효한인덱스+1 이하이면 자동적으로 i+K+1 반환
        for j in range(max(0, i - K), min(N, i + K + 1)):
            if tableList[j] == 'H':  # 먹을 수 있는 햄버거 발견 시
                tableList[j] = 'X'  # 먹은 햄버거 표시
                count += 1
                break  # 햄버거 하나 먹었으니 다음 사람으로



# 3. 결과 출력
print(f" total count : {count}\n")
