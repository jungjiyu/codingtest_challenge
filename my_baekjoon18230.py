from sys import stdin, stdout

input = stdin.readline
print = stdout.write


# 1.인풋값 받기
N, A, B = map(int,input().split())
TwoByOneList = list(map(int,input().split()))
TwoByTwoList = list(map(int,input().split()))
# 2.각 리스트 sort
TwoByOneList.sort(reverse=True)
TwoByTwoList.sort(reverse=True)
#print(f"N:{N},A:{A},B:{B},TwoByOneList:{TwoByOneList},TwoByTwoList:{TwoByTwoList}\n")

# 3.예쁨지수최대되게 배치

totalBeauty=0
curTwoByOneIdx=0
curTwoByTwoIdx=0
if N%2 ==1:
    totalBeauty+=TwoByOneList[curTwoByOneIdx]
    TwoByOneList[curTwoByOneIdx]=0
    curTwoByOneIdx+=1
    N-=1
#    print(f"N is odd , changed -> N:{N},TwoByOneList:{TwoByOneList}, totalBeauty:{totalBeauty}\n")

for k in range(N//2):
    curTwoByOneListVal =0
    curTwoByTwoListVal = 0
    if (curTwoByOneIdx+1<A):
        curTwoByOneListVal=TwoByOneList[curTwoByOneIdx]+TwoByOneList[curTwoByOneIdx+1]

    if (curTwoByTwoIdx<B):
        curTwoByTwoListVal=TwoByTwoList[curTwoByTwoIdx]

    if (curTwoByOneListVal>curTwoByTwoListVal):
        totalBeauty += curTwoByOneListVal
        TwoByOneList[curTwoByOneIdx] = 0
        curTwoByOneIdx += 2
    else :
        totalBeauty += curTwoByTwoListVal
        TwoByTwoList[curTwoByTwoIdx] = 0
        curTwoByTwoIdx += 1
#    print(f" changed -> N:{N},TwoByOneList:{TwoByOneList},TwoByTwoList:{TwoByTwoList}, totalBeauty:{totalBeauty}\n")

# 4.결과출력
print(f"{totalBeauty}\n")
