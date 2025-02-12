import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input().strip())
costs = [list(map(int, input().split())) for _ in range(N)] # 0 == 빨 , 1 == 초 , 2 == 파
print(f"costs:{costs}\n")


# idx == 행, prev_color == 열
def brute(idx, prev_color):
    # 모든 집을 칠한 경우
    if idx == N :
        return 0

    # 걍 ㅈㄴ 큰 수로 초기화
    min_cost = 2000*N 
    
    
    for color  in range(3):
        if color != prev_color:  # 이전 단계 cost 값 안겹치게 둘 중 하나
            cur_cost = costs[idx][color]  + brute(idx+1,color) # 다음 단계도 구함
            min_cost=min(min_cost,cur_cost) # 이전 단계 cost 값 적용된 것 중 더 작은 값 택

    return min_cost




# 점화식 : table[i][j] = inputList[ i ][ j] + min( table[ i -1][ j아닌값1 ] , table[ i-1 ][ j아닌값2 ] )


# table 전체를 저장하는 케이스
def bottmUp():
    table = [[0 for _ in range(3)] for _ in range(N)]
    # 기저상태
    table[0] = costs[0]
    print(f"tableInit : {table}\n")
    for i in range(1,N):
        table[i][0] = min(table[i - 1][1], table[i - 1][2]) + costs[i][0]
        table[i][1] = min(table[i - 1][0], table[i - 1][2]) + costs[i][1]
        table[i][2] = min(table[i - 1][0], table[i - 1][1]) + costs[i][2]
        
    print(f"result table : {table}\n")
    print(f"{min(table[-1])}\n")
    


# 마지막만 끌고가는 케이스
def bottmUp2():
    # 기저상태
    table = costs[0].copy()
    print(f"tableInit : {table}\n")

    for i in range(1,N):
        table = [
            min(table[1], table[2]) + costs[i][0],
            min(table[0], table[2]) + costs[i][1],
            min(table[0], table[1]) + costs[i][2]
        ]

    print(f"result table : {table}\n")

    print(f"{min(table)}")



def main():

    # 완전탐색으로 구현
    # result = brute(0,-1)
    # print(f"{result}\n")


    #DP 로 구현
    bottmUp()
    bottmUp2()
    return

if __name__ == "__main__":
    main()