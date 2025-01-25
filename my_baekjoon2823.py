from sys import stdin,stdout

input = stdin.readline
print = stdout.write


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def is_dead_end(R, C, TownMap):
    # 막다른 길 확인
    for y in range(R):
        for x in range(C):
            if TownMap[y][x] == '.':
                # print(f"(x,y)=({x},{y})\n")
                path_count = 0
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < R and 0 <= nx < C and TownMap[ny][nx] == '.':
                        path_count += 1
                if path_count < 2:  # 막다른 길이 발견됨
                    return True
    return False


def main():

    # 입력
    R, C = map(int, input().split())
    TownMap = [list(input().strip()) for _ in range(R)]

    # 막다른 길 여부 판단
    if is_dead_end(R, C, TownMap):
        print("1\n")  # 막다른 길 있음
    else:
        print("0\n")  # 막다른 길 없음


if __name__ == "__main__":
    main()
