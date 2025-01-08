##문제
# N개의 정수로 이루어진 수열이 있을 때, 크기가 양수인 부분수열 중에서 그 수열의 원소를 다 더한 값이 S가 되는 경우의 수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 정수의 개수를 나타내는 N과 정수 S가 주어진다. (1 ≤ N ≤ 20, |S| ≤ 1,000,000) 둘째 줄에 N개의 정수가 빈 칸을 사이에 두고 주어진다. 주어지는 정수의 절댓값은 100,000을 넘지 않는다.
#
# 출력
# 첫째 줄에 합이 S가 되는 부분수열의 개수를 출력한다.
#
# 예제 입력 1
# 5 0
# -7 -3 -2 5 8
# 예제 출력 1
# 1





from sys import stdin, stdout

input = stdin.readline
print = stdout.write

# 1. input 값 N과 S , 원소 받기
N, S = map(int, input().split())
print(f"N:{N} , S:{S}\n")
originSequence = list(map(int,input().split()))


count = 0

for d in range(1, (2**N-1)+1): # 0000 .. ~ 1111.. , 공집합 미포함
    # 2. 부분 수열 구하기
    partSequence = []
    binary_string_without_prefix = bin(d)[2:].zfill(N)  # '0b1010' ->  '1010'
    print(f"binary_string_without_prefix: {binary_string_without_prefix}\n")  # 출력: 1010
    for i in range(len(binary_string_without_prefix)):
        if binary_string_without_prefix[i] == "1":
            partSequence.append(originSequence[i])
    print(f"partSequence: {partSequence}\n")
    partSequenceSum = sum(partSequence)
    print(f"partSequenceSum: {partSequenceSum}\n")
    # 3. 해당 부분수열의 원소 sum 과 S 비교하기
    if partSequenceSum == S:
        count+=1
        print(f"count updated:{count}\n")


# 4. 결과 출력
print(f"count:{count}\n")



