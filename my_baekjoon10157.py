from sys import stdin, stdout,exit

input = stdin.readline
print = stdout.write



# 2. 좌석에 대기번호 부여
# 3. 특정 좌석의 대기번호 구하기 및 결과출력
def find_seat(C, R, K):
    #seat =[[0]*C for _ in range(R)]
    #print(f"seat:{seat}\n")
    numberTicket=1
    layer =0 # 사이클 회차

    while(numberTicket <= R*C):
        # 위쪽
        for i in range(layer ,R - layer ):
    #        seat[i][layer] = numberTicket
            if(numberTicket==K):
                return f"{layer + 1} {i + 1}"
            numberTicket+=1
    #    print(f"    with up :{seat}\n")

        # 오른쪽
        for j in range(layer+1,C - layer):
    #        seat[R - layer - 1][j] = numberTicket
            if(numberTicket==K):
                return f"{j + 1} {R - layer - 1+1 }"
            numberTicket+=1
    #    print(f"    with right :{seat}\n")

        # 아래쪽
        for i in reversed(range(layer,R-(layer+1))):
    #        seat[i][C - layer - 1] = numberTicket
            if(numberTicket==K):
                return f"{C - layer- 1+1} {i + 1}"
            numberTicket+=1
    #    print(f"    with down :{seat}\n")

        #왼쪽
        for j in reversed(range(layer+1,C-(layer+1))):
    #        seat[layer][j] = numberTicket
            if(numberTicket==K):
                return f"{j + 1} {layer + 1}"
            numberTicket+=1
    #    print(f"    with left :{seat}\n")

        layer += 1  # 다음 레이어로 이동
    #    print(f"updated seat:{seat}\n")

    #print(f"final seat:{seat}\n")
    return "0"

def main():
    # 1. input값 입력받기
    C, R = map(int, input().split())
    K = int(input())
    #print(f"C:{C},R:{R},K:{K}\n")    result = find_seat(C, R, K)
    result = find_seat(C, R, K)
    print(result)

if __name__ == "__main__":
    main()
