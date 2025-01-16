from sys import stdin, stdout, exit

input = stdin.readline
print = stdout.write
R,C = 0,0
originalMap=[]
sinkPositionList=[]





def isIndexValid(i,j):
    global R,C
    if (i<0 or j<0 or i>=R or j>=C):
        return False
    return True



def checkSink(i, j):
    global originalMap, sinkPositionList

    if originalMap[i][j] != 'X':
        return  # 'X'가 아니면 검사하지 않음

    count = 0
    # 오른쪽
    if isIndexValid(i, j + 1):
        if originalMap[i][j + 1] == ".":
            count += 1
    else:
        count += 1  # 맵 외부는 바다로 간주

    # 위쪽
    if isIndexValid(i - 1, j):
        if originalMap[i - 1][j] == ".":
            count += 1
    else:
        count += 1  # 맵 외부는 바다로 간주

    # 왼쪽
    if isIndexValid(i, j - 1):
        if originalMap[i][j - 1] == ".":
            count += 1
    else:
        count += 1  # 맵 외부는 바다로 간주

    # 아래쪽
    if isIndexValid(i + 1, j):
        if originalMap[i + 1][j] == ".":
            count += 1
    else:
        count += 1  # 맵 외부는 바다로 간주

    if count >= 3:
        sinkPositionList.append([i, j])


def doSink():
    global originalMap, sinkPositionList
    for e in sinkPositionList:
        originalMap[e[0]][e[1]] ='.'
#    print(f"map updated with sink :{originalMap}\n")


def trimAndPrintMap():
    global R,C,originalMap
    min_row = max_row = min_col = max_col = -1
    for i in range(R):
        for j in range(C):
            if originalMap[i][j] == "X":
                if min_row == -1:
                    min_row = max_row = j
                    min_col = max_col = i
                    continue
                if i < min_col:
                    min_col = i
                elif i > max_col:
                    max_col = i
                if j < min_row:
                    min_row = j
                elif j > max_row:
                    max_row = j

    # 결과 출력
    for i in range(min_col, max_col + 1):
        row_str = ''.join(originalMap[i][min_row:max_row + 1])
        print(row_str + "\n")

def travelMap():
    global R,C,originalMap
    # 2. 지도 순회 및 잠길 위치 구하기
    for i in range(R):
        for j in range(C):
            checkSink(i,j)
    # 3. 잠김 처리
    doSink()

    # 4. 최종 지도 출력
    trimAndPrintMap()



def main():
    global R,C,originalMap
    # 1. input값 입력받기
    R, C = map(int, input().split())
    for k in range(R):
        tmpRow = list(input().strip())
        originalMap.append(tmpRow)
#    print(f"R:{R},C:{C},originalMap:{originalMap}\n")
    travelMap()


if __name__ == "__main__":
    main()