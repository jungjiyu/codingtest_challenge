from sys import stdin, stdout

input = stdin.readline
print = stdout.write
maxResult = None
minResult = None

# 1. K 와 부등호 나열 입력받기
K = int(input().strip())
InequalitySignList = list(input().strip().split())


def backtracking(curPermutation, used, depth):
    global maxResult, minResult

    # 3. 최댓값과 최솟값 구하기
    if depth == K + 1:     # K+1 자리 숫자가 완성된 경우
        curPermutationStr = ''.join(map(str, curPermutation))

        if maxResult is None or curPermutationStr > maxResult:
            maxResult = curPermutationStr
        if minResult is None or curPermutationStr < minResult:
            minResult = curPermutationStr
        return

    #2. 부등호나열을 만족하는 숫자 구하기
    for n in range(10):
        if not used[n]:
            # 부등호 조건 확인
            if depth == 0 or (
                    InequalitySignList[depth - 1] == '<' and curPermutation[-1] < n) or (
                    InequalitySignList[depth - 1] == '>' and curPermutation[-1] > n):
                # 숫자 사용
                used[n] = True
                curPermutation.append(n)
                backtracking(curPermutation, used, depth + 1)

                # 백트래킹
                curPermutation.pop()
                used[n] = False


# 4. 구한 최댓값과 최솟값 출력
used = [False] * 10
backtracking([], used, 0)
print(f"{maxResult}\n{minResult}\n")
