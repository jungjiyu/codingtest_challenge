import sys

input = sys.stdin.readline
print = sys.stdout.write

T=int(input())
inputList= [ int(input()) for _ in range(T)]
# print(f"inputList:{inputList}\n")

# 점화식 : DP[i] = DP[i-3] + DP[i-2] + DP[i-1]

# 단순 브루트포스 구현
# 일단 1 ,2,3 을 넘치치 않을떄까지 계속 더함
def brute(cursum,goal):

    if cursum ==goal:
        # print(f"    cursum ==goal curSum:{cursum}\n")
        return 1

    if cursum > goal:
        # print(f"    cursum > goal -curSum:{cursum}\n")
        return 0

    # print(f"    else -curSum:{cursum}\n")
   # 1, 2, 3을 더하는 3가지 선택
    return (
        brute(cursum+1, goal)+
        brute(cursum+2, goal)+
        brute(cursum+3, goal)
    )





# 반복문 통한 dp 구현
table = [0]*11 # 11 이 최대 사이즈 : 11 까지 표현 가능한데, 11 의 경우 1*11 이니까
def bottmUp():
    global table

    # 기저상태
    table[0]=1
    table[1]=2
    table[2]=4

    for i in range(3,11):
        table[i]=table[i-1]+table[i-2]+table[i-3]
    # print(f"tablization complete : {table}\n")



# 재귀 통한 dp 구현
memo=[0]*12 # 편의상 인덱스 0은 사용하지 않음
# 기저상태 처리
memo[1] = 1
memo[2] = 2
memo[3] = 4
def topDown(n):
    global memo

    if n==1:
        print(f"    n == 1\n")
        return 1

    if n==2:
        print(f"    n == 2\n")
        return 2

    if n==3:
        print(f"    n == 3\n")
        return 4

    # memoization 활용
    # 메모된 적 있는 값이면 그 값을 바로 활용
    if memo[n] != 0 :
        return memo[n]

    # 메모된적 없으면 새로 구하기 및 기록
    memo[n] = topDown(n-1) + topDown(n-2) + topDown(n-3)
    return memo[n]



def main():
    # 브루트 포스 시도
    # for i in range(T):
    #     val=brute(0,inputList[i])
    #     print(f"{val}\n")

    # DP 시도 : 반복문 구현
    # bottmUp()
    # for i in range(T):
    #     val=table[ inputList[i]-1 ]
    #     print(f"{val}\n")


    # DP 시도 : 재귀 구현
    topDown(11)
    print(f"memo:{memo}\n")
    for i in range(T):
        val=memo[ inputList[i] ]
        print(f"{val}\n")



if __name__ == "__main__":


    main()
