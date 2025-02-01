from sys import stdin, stdout

input = stdin.readline
print = stdout.write

# 위 오 아래 왼
dx = [0,1,0,-1]
dy = [-1,0,1,0]
N=0


def swapCandy(y,x,ny,nx,candyMatrix):
    global N

    if candyMatrix[y][x] != candyMatrix[ny][nx]:
        tmp = candyMatrix[y][x]
        candyMatrix[y][x]= candyMatrix[ny][nx]
        candyMatrix[ny][nx] = tmp
        curMaxCount=getMaxStraightCandy(candyMatrix)
        # print(f"candy swapped ({y},{x})<-->({ny},{nx}): {candyMatrix}\n")

        # 최대 연속 갯수 구하고 원본 복구
        tmp = candyMatrix[y][x]
        candyMatrix[y][x]= candyMatrix[ny][nx]
        candyMatrix[ny][nx] = tmp
        return curMaxCount
    # print(f"candy not sawpped\n")
    return -1

def getMaxStraightCandy(candyMatrix):
    global N


    # 3. 각 상황별 max 갯수 구함
    maxStraightCandyCount = 0



    for y in range(N):
        rowStraightCount = 1
        for x in range(N-1):
            if(candyMatrix[y][x] == candyMatrix[y][x+1]):
                rowStraightCount+=1
                if rowStraightCount > maxStraightCandyCount:
                    maxStraightCandyCount = rowStraightCount

            else :
                rowStraightCount = 1 # 초기화. 새로운 색깔 시작.


    # print(f"maxStraightCandyCount:{maxStraightCandyCount}\n")


    # 열 방향 최대 연속
    for x in range(N):
        colStraightCount = 1
        for y in range(N-1):
            if(candyMatrix[y][x] == candyMatrix[y+1][x]):
                colStraightCount+=1
                if colStraightCount > maxStraightCandyCount:
                    maxStraightCandyCount = colStraightCount
            else :
                colStraightCount = 1 # 초기화. 새로운 색깔 시작.

    # print(f"maxStraightCandyCount:{maxStraightCandyCount}\n")

    return maxStraightCandyCount




def main():
    global N
    # 1. input 값 받기
    N = int(input())
    candyMatrix = [ list(input().strip()) for _ in range(N)]
    # print(f"N:{N},candyMatrix:{candyMatrix}\n")
    maxCandyCount=getMaxStraightCandy(candyMatrix)

    for y in range(N):
        for x in range(N):
            # 2. 오른쪽과 아래쪽만 탐색해 swap 가능 여부 판단
            for i in range(2):
                ny = y + dy[i]
                nx = x + dx[i]
                if  0<=ny<=N-1 and 0<=nx<=N-1  :
                    curMaxCount= swapCandy(y, x, ny, nx,candyMatrix)
                    if  curMaxCount > maxCandyCount :
                        maxCandyCount = curMaxCount


    # print(f"final result :{maxCandyCount}\n")
    print(f"{maxCandyCount}\n")



# 4. 출력하기

if __name__ == "__main__":
    main()
