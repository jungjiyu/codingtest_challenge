from sys import stdin, stdout

input = stdin.readline
print = stdout.write




# 2. 모든쌓을수있는케이스구하기(위 아래 어떻게 배치될 수 있나)
# 위 아래로 회전하기
def turnVertical(originDice):
    dice = originDice.copy()

    # 90도 회전
    dice[0] = originDice[2]
    dice[5] = originDice[4]
    dice[2] = originDice[5]
    dice[4] = originDice[0]

#    print(f"vertical rotate 90 :{dice}\n")

    return dice


# 양 옆으로 회전하기
def turnHorizontal(originDice):
    dice = originDice.copy()

    # 90도 회전
    dice[1] = originDice[2]
    dice[2] = originDice[3]
    dice[3] = originDice[4]
    dice[4] = originDice[1]

#    print(f"horizontal rotate 90 :{dice}\n")

    return dice



# 주사위 쌓기
def stackDice( criteria , dice): # 맨 밑이 criteria 값이 될때까지 회전

    if dice[5] == criteria:
        return dice

    # 수직 방향 회전
    for _ in range(3):
        dice= turnVertical(dice)
        if dice[5] == criteria :
            return dice

    # 수평 방향 회전 1회
    dice=turnHorizontal(dice)

    # 수직 방향 회전
    for _ in range(3):
        dice=turnVertical(dice)
        if dice[5] == criteria :
            return dice


def getMaxSideValue(dice):
    # 수직 방향 회전
    maxSideVaule = dice[1]
    for i in range(2,5):
        if dice[i] > maxSideVaule :
            maxSideVaule=dice[i]

    return maxSideVaule



def main():
    # 1. input값입력받기
    N = int(input())  # 주사위 갯수
    dices = []  # 주사위들
    for i in range(N):
        nthDice = list(map(int, input().split()))
        dices.append(nthDice)
#    print(f"N:{N}, dices :{dices}\n")

    # 2. 쌓을 수 있는 모든 경우 구하기
    possibleAllocatoins = []

    for i in range(1,6+1):
        diceAllocation=[]
        # 첫번째 dice 쌓기
        firstDiceAllocation = stackDice(i,dices[0])
#        print(f"first dice : {firstDiceAllocation}\n")
        diceAllocation.append(firstDiceAllocation)

        # 첫번쨰 dice 기준으로 나머지 dice 들 쌓기
        for j in range(1,N):
            nthDiceAllocation = stackDice(diceAllocation[j-1][0], dices[j])
            diceAllocation.append(nthDiceAllocation)
        possibleAllocatoins.append(diceAllocation)
#        print(f"possibleAllocatoins added : {possibleAllocatoins}\n")

#    print(f"final possibleAllocatoins : {possibleAllocatoins}\n")

    # 4. 통틀어 최댓값 구하기
    finalMaxSum = 0
    for allocation in possibleAllocatoins:
        # 3. 모든쌓을수있는케이스별로최댓값구하기( 각 주사위를 옆으로 어떻게 돌릴 수 있나)
        nthSum = 0
        for nthDice in allocation:
            nthSum += getMaxSideValue(nthDice)

        if finalMaxSum == 0  or finalMaxSum < nthSum :
            finalMaxSum = nthSum

    print(f"{finalMaxSum}\n")
    # 5. 결과 출력
if __name__ == "__main__":
    main()