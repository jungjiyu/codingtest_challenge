from sys import stdin


def main():
    # 입력 받기
    N = int(stdin.readline())
    totalRecommendationCount = int(stdin.readline())
    recommendedStudentList = list(map(int, stdin.readline().split()))

    photoList = []  # 각 요소는 [학생id, 추천수, 게시된 시퀀스]
    currentSeq = 0  # 시퀀스 번호를 관리

    for student in recommendedStudentList:
        found = False
        # 이미 사진틀에 있는지 확인
        for photo in photoList:
            if photo[0] == student:
                photo[1] += 1
                found = True
                break
        if not found:
            if len(photoList) < N:
                # 사진틀에 빈 공간이 있을 경우 추가
                photoList.append([student, 1, currentSeq])
                currentSeq += 1
            else:
                # 사진틀이 꽉 찼을 경우 삭제할 학생 결정
                # 추천수 최솟값 찾기
                min_recommend = min(photoList, key=lambda x: (x[1], x[2]))[1]
                # 추천수가 최소인 학생들 중 가장 오래된 학생 찾기
                candidates = [photo for photo in photoList if photo[1] == min_recommend]
                # 가장 오래된 시퀀스 번호를 가진 학생
                oldest = min(candidates, key=lambda x: x[2])
                # 삭제
                photoList.remove(oldest)
                # 새 학생 추가
                photoList.append([student, 1, currentSeq])
                currentSeq += 1

    # 최종 사진틀에 있는 학생들 번호를 오름차순으로 정렬하여 출력
    final_candidates = sorted([photo[0] for photo in photoList])
    print(' '.join(map(str, final_candidates)))


if __name__ == "__main__":
    main()
