from sys import stdin,stdout
from collections import deque
import time

input = stdin.readline
print = stdout.write







# 위 오 아 왼 대각1 대각2 대각3 대각4
dx =[0,1,0,-1,1,1,-1,-1]
dy = [-1,0,1,0,-1,1,-1,1]

def checkLand(y,x,w,h,mapList):
    # print(f"    checkLand input:{y},{x}\n")
    if  0<= y <h and 0<=x<w  :
        if mapList[y][x] == 1:
            # print(f"this is land\n")
            return True

    # 지도를 벗어나면 바다
    # mapList 값이 0 인 경우 바다
    # print(f"this is ocean\n")
    return False




def bfs(y,x,w,h,mapList,visited):
    # print(f"bfs input:{y},{x}\n")
    queue = deque()


    # 초기화
    queue.append([y,x])
    visited[y][x]=True

    while queue:
        curY,curX=queue.popleft()

        # 인근 조사
        for i in range(8):
            tmpX = dx[i]+curX
            tmpY= dy[i] + curY
            isLand = checkLand(tmpY, tmpX,w,h,mapList)
            # time.sleep(0.3)

            if isLand and not visited[tmpY][tmpX]:
                queue.append([tmpY,tmpX])
                visited[tmpY][tmpX]=True




def main():
    w, h = map(int, input().split())

    while w!=0 and h!=0:
        mapList = [list(map(int, input().split())) for _ in range(h)]
        # print(f"mapList:{mapList}\n")
        visited = [[False] * w for _ in range(h)]
        # print(f"init visited:{visited}\n")

        islandCount = 0
        for j in range(h):
            for i in range(w):
                isLand = checkLand(j, i,w,h,mapList)

                if isLand and not visited[j][i]:
                    bfs(j,i,w,h,mapList,visited)
                    islandCount+=1
        print(f"{islandCount}\n")

        w, h = map(int, input().split())

if __name__=="__main__":
    main()

