import math
import sys

input= sys.stdin.readline
print = sys.stdout.write



N, M= map(int, input().split())
inputList = [list(map(int, input().split())) for _ in range(N)]
# print(f"inputList:{inputList}\n")

def getTimeComplex():
    n=m=300
    # 조합 모듈을 직접 사용
    result = math.comb(n + m - 2, n - 1)
    print(f"brute : {result}\n") # ㅈㄴ 큼



# 구글링 풀이
table=[[0]*(M+1) for _ in range(N+1)]
def bottmUp():
    global table
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            table[i][j] = inputList[i - 1][j - 1] + max(table[i - 1][j], table[i][j - 1])
            # print(f"table:{table}\n")
            # print(f"    input :{inputList[i - 1][j - 1]}, table 왼 :{table[i][j - 1]}, table 아 :{table[i - 1][j]} , max :{max(table[i - 1][j], table[i][j - 1])}\n")

    print(f"{table[-1][-1]}\n")



#  멘토 제공 풀이
def bottmUp2():
    # 2. DP 탐색을 위한 초기화를 합니다.
    DP = [[0 for _ in range(M)] for _ in range(N)]


    # 3. 세운 점화식에 맞게 DP 탐색을 진행합니다.
    for i in range(N):
        for j in range(M):
            if i == 0 and j == 0:
                DP[i][j] = inputList[i][j]
            elif i == 0:
                DP[i][j] = DP[i][j - 1] + inputList[i][j]
            elif j == 0:
                DP[i][j] = DP[i - 1][j] + inputList[i][j]
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) + inputList[i][j]

    # 4. 최종 위치에서의 값을 출력합니다.
    print(f"{DP[N - 1][M - 1]}\n")


def main():
    # getTimeComplex()
    bottmUp()
    # bottmUp2()
    return

if __name__ ==  "__main__":
    main()