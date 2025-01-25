from sys import stdin,stdout

input = stdin.readline
print = stdout.write


def getClockwiseNumber(cardNumbers):
    clockwiseNumbers = []

    # 2.최소 시계수 찾기
    for i  in range(4):
        curStrNum=""
        for j in range(4):
            curStrNum += str(cardNumbers[(j+i) %4])
        clockwiseNumbers.append(int(curStrNum))
    # print(f"cardNumbers:{cardNumbers}, clockwisNumvers : {clockwiseNumbers}\n")

    minClockwiseNumber = min(clockwiseNumbers)
    # print(f"minClockwiseNumber: {minClockwiseNumber}\n")
    return minClockwiseNumber

def main():
    # 1.input 받기
    cardNumbers = input().split()
    targetMinClockwiseNumber = getClockwiseNumber(cardNumbers)

    # 3.더 작은 시계수들 & 개수 구하기
    clockwiseNumbers=[]
    count = 1

    for target in range(1111,targetMinClockwiseNumber):
        targetStrList = list(str(target))
        if "0" not in targetStrList:
            curMinClockwiseNumber = str(getClockwiseNumber(targetStrList))
#            print(f"curMinClockwiseNumber: {curMinClockwiseNumber} -> ")
            if curMinClockwiseNumber in clockwiseNumbers:
#                print(f"    already exists : {target}\n")
                continue
#            print(f"    new count : {target}\n")
            count+=1
            clockwiseNumbers.append(curMinClockwiseNumber)
    # 3.시계수 - 1111 +1출력
#    print(f"{clockwiseNumbers}, ")
    print(f"{count}")


if __name__ == "__main__":
    main()