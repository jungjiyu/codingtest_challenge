# 문제
# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다. 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다. 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.
#
# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 다섯 개의 줄에 다섯 개의 정수로 숫자판이 주어진다.
#
# 출력
# 첫째 줄에 만들 수 있는 수들의 개수를 출력한다.
#
# 예제 입력 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 1 1
# 1 1 1 2 1
# 1 1 1 1 1
# 예제 출력 1
# 15









from sys import stdin, stdout
input = stdin.readline
print = stdout.write
N=5
numberBoardList = []
foundSixDigitSet = set()

# 2. 가능한 6자리숫자 탐색 및 unique set 업데이트
def dfsNumberBoard(count, curDigit , i,j):
    global numberBoardList
    global foundSixDigitSet
    print(f"count :{count}, curDigit:{curDigit}, i : {i},j:{j}\n")

    if i <0 or j<0 or N-1<i or N-1 < j:
        print("i <0 or j<0 or N-1<i or N-1 < j\n")
        return

    # 종료 조건
    if count == 6 :
        if not (curDigit in foundSixDigitSet):
            foundSixDigitSet.add(curDigit)
            print(f"foundSixDigitSet updated:{foundSixDigitSet}\n")
        return




    curDigit = curDigit + str(numberBoardList[i][j])

    dfsNumberBoard(count+1,curDigit,i-1,j) #위
    dfsNumberBoard(count+1,curDigit,i,j+1) #오
    dfsNumberBoard(count+1,curDigit,i+1,j) #아래
    dfsNumberBoard(count+1,curDigit, i,j-1) #왼


# 1. 숫자판 구성 숫자들 input으로 받기
for i in range(N):
    rowList = list(map(int,input().split()))
    print(f"{i}th row : {rowList}\n ")
    numberBoardList.append(rowList)
print(f"numberBoardList : {numberBoardList}\n")


# 3. 결과 출력

for i in range(N):
    for j in range(N):
        dfsNumberBoard(0, "", i, j)
print(f"result: {len(foundSixDigitSet)}\n")