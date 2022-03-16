from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 인풋 받기
for tc in range(1, T + 1):
    N = int(input())

    # string 타입으로 받아주기! > 순회하면서 1씩 증가시킬거라 int로 받으면 도착지 설정에 문제
    miro = [list(input()) for _ in range(N)]

    # 시작점 찾는 함수
    def find_start(arr):
        for i in range(N):
            for j in range(N):
                if arr[i][j] == '2':
                    arr[i][j] = 1
                    return i, j

    # 도착점 찾는 함수
    def check(c, r):
        q = deque()
        q.append((c, r))

        # q가 빌 때까지 순회하면서
        while q:
            dc = [0, 0, 1, -1]
            dr = [1, -1, 0, 0]

            c, r = q.popleft()

            for i in range(4):
                nc = c + dc[i]
                nr = r + dr[i]

                # 인덱스 범위 안의 '0' 이면 q에 추가
                if 0 <= nc < N and 0 <= nr < N and miro[nc][nr] == '0':
                    miro[nc][nr] = miro[c][r] + 1
                    q.append((nc, nr))

                # 범위 안의 '3' 이면 도착지이므로 리턴
                elif 0 <= nc < N and 0 <= nr < N and miro[nc][nr] == '3':
                    return miro[c][r]

        # 도착지를 찾지못하면 1 리턴
        return 1

    # 함수를 실행하고 결과 값에서 -1을 해준다, > 출발지가 포함되었기 때문
    se = find_start(miro)
    print(f'#{tc} {check(se[0], se[1]) - 1}')

