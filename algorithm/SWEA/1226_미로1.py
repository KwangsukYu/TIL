from collections import deque
import sys
sys.stdin = open('input.txt')

# 도착 가능한지 확인하는 함수
def check(g, s):

    # deque를 설정해주고 시작 좌표를 넣어주기
    queue = deque()
    queue.append((g, s))

    # 4방향 탐색
    dc = [0, 0, 1, -1]
    dr = [1, -1, 0, 0]

    # 갈 수 있는 곳이 있으면
    while queue:

        # queue의 왼쪽부터 뽑아주기 > BFS
        c, r = queue.popleft()

        # 4방향을 돌면서
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]

            # 인덱스 범위 안에 0이면 갈 수 있는 경로이므로
            if 0 <= nc < 16 and 0 <= nr < 16 and not arr[nc][nr]:

                # 방문 확인용으로 1을 추가하고
                arr[nc][nr] += 1
                # 다시 queue에 넣어주기
                queue.append((nc, nr))

            # 만약 도착지에 도착을 한다면 1을 리턴
            elif 0 <= nc < 16 and 0 <= nr < 16 and arr[nc][nr] == 3:
                return 1
    # 다 돌았는데 도착하지 못했다면 0을 리턴
    return 0

# 인풋 받기
for tc in range(1, 11):
    t = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    # 결과 출력
    # print(f'#{t} {check(1, 1)}')


