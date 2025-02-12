import sys

input = sys.stdin.readline
print = sys.stdout.write

M,n = map(int,input().split())
print(f"M,n:{M},{n}\n")



# 0, 1, 2, 3 인덱스 == 위 오 아 왼 <-- 위쪽 왼쪽 모서리가 0,0 이 아닌 아래쪽 왼쪽 모서리가 0,0 임을 주의
dx = [ 0, 1, 0, -1 ]
dy = [ 1, 0, -1, 0 ]

# 현재 좌표
curX=curY=0
# 오른쪽에서 보고 시작
curDirection = 1


def moveIfPossible(str_code , int_code):
    global curX,curY , curDirection
    if str_code == "MOVE":
        tmpX = curX
        tmpY = curY
        for i in range( int(int_code) ):
            tmpX +=dx[curDirection]
            tmpY += dy[curDirection]

        if (0<tmpX<M) and (0<tmpY<M):
            curX=tmpX
            curY=tmpY
            print(f"curY,curX updated : {curY},{curX}\n")
            return True



    elif str_code == "TURN":
        for i in range( int(int_code) ):
            curDirection = (curDirection+1)%4
            print(f"curDirection updated : {curDirection}\n")
        return True

    print(f"index out of range keep goin\n")
    return False




def main():
    for i in range(n):
        str_code , int_code= input().strip().split()
        print(f"{str_code}, {int_code}\n")
        moveIfPossible(str_code,int_code)

    if (0 < curX < M) and (0 < curY < M):
        print(f"{curX} {curY}\n")
    print(f"-1\n")


   


if __name__ == "__main__":
    main()
