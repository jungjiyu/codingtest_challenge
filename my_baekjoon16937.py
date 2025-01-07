# 문제 : 두 스티커
    # 크기가 H×W인 모눈종이와 스티커 N개가 있다. i번째 스티커의 크기는 Ri×Ci이다. 모눈종이는 크기가 1×1인 칸으로 나누어져 있으며, 간격 1을 두고 선이 그어져 있다.
    #
    # 오늘은 모눈종이에 스티커 2개를 붙이려고 한다. 스티커의 변은 격자의 선과 일치하게 붙여야 하고, 두 스티커가 서로 겹치면 안 된다. 단, 스티커가 접하는 것은 가능하다. 스티커를 90도 회전시키는 것은 가능하다. 스티커가 모눈종이를 벗어나는 것은 불가능하다.
    #
    # 두 스티커가 붙여진 넓이의 최댓값을 구해보자.

# 입력
    # 첫째 줄에 모눈종이의 크기 H, W, 둘째 줄에 스티커의 수 N이 주어진다. 다음 N개의 줄에는 스티커의 크기 Ri, Ci가 주어진다.

# 출력
#     첫째 줄에 두 스티커가 붙여진 넓이의 최댓값을 출력한다. 두 스티커를 붙일 수 없는 경우에는 0을 출력한다.

# 제한
#      1 ≤ H, W, N ≤ 100
#      1 ≤ Ri, Ci ≤ 100



##try1
# from sys import stdin, stdout
#
# input = stdin.readline
# print = stdout.write
# H,W = map(int,input().split())
# print(f"H:{H},W:{W}\n")
#
# N = int(input())
# print(f"N:{N}\n")
#
# stickers=[]
# for i in range(N):
#     sticker = list(map(int, input().split()))
#     stickers.append(sticker)
#
# print(f"raw stickers:{stickers}\n")
# stickers.sort(key=lambda x: x[0] * x[1], reverse=True) # 첫요소*두번쨰요소 값 기준 내림차순 정렬
# print(f"sorted stickers :{stickers}\n")
#
# result=0
# totalSize=H*W
# for i in range(N):
#     # 1. 모눈종이 넓이 이상이면 나가리
#     firstSticker = stickers[i]
#     firstStickerSize = firstSticker[0] * firstSticker[1]
#     if firstStickerSize >= totalSize:
#         print(f"firstSticker is too large\n")
#         continue
#
#     # 뒷 얘들 중 가능한 조합 있나 확인
#     for k in range(i+1, N):
#         secondSticker = stickers[k]
#         secondStickerSize = secondSticker[0] * secondSticker[1]
#
#         print(f"firstStickerSize :{firstStickerSize}, secondStickerSize : {secondStickerSize}\n")
#         if totalSize >=firstStickerSize + secondStickerSize: # 2. 둘 합친 넓이가 모눈 종이 이하면
#             r1 , c1 = firstSticker
#             r2, c2=secondSticker
#
#             if  ((r1+r2 <=H ) and (c1+c2<=W)) or  ((r1+r2 <=W ) and (c1+c2<=H))or ((r1+c2 <=H ) and (c1+r2<=W)) or ((r1+c2 <=W ) and (c1+r2<=H)): # 둘이 겹치지 않으면
#                 result = firstStickerSize + secondStickerSize
#                 break
#
#             else :
#                 print("stickers duplicated\n")
#     if result !=0:
#         break
# print(f"result :{result}\n")


##try2
H, W = map(int, input().split())
N = int(input())
stickers = [list(map(int, input().split())) for _ in range(N)]

# 스티커 넓이를 기준으로 내림차순 정렬
stickers.sort(key=lambda x: x[0] * x[1], reverse=True)

result = 0

for i in range(N):
    r1, c1 = stickers[i]
    firstStickerSize = r1 * c1
    if firstStickerSize >= H * W:
        continue

    for k in range(i + 1, N):
        r2, c2 = stickers[k]
        secondStickerSize = r2 * c2

        if firstStickerSize + secondStickerSize <= result:
            # 현재 최대 넓이보다 작은 조합은 무시
            continue

        # 두 스티커의 배치 경우를 체크
        for a, b in [(r1, c1), (c1, r1)]:
            for x, y in [(r2, c2), (c2, r2)]:
                # 배치 가능한 경우
                if (a + x <= H and max(b, y) <= W) or (b + y <= W and max(a, x) <= H):
                    result = max(result, firstStickerSize + secondStickerSize)

print(result)
