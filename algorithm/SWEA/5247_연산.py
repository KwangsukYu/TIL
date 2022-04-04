import sys
sys.stdin = open('sample_input.txt')

from collections import deque

# BFS로 최소 연산 횟수 구하기
def check(s):

    # q는 덱 설정 후 시작 값 N과 cnt 0을 튜플로 넣어줌
    q = deque()
    q.append((s, 0))

    # q가 빌 때까지 순회
    while q:

        # 튜플 형식으로 저장 되어 있는 원소를 ssum 과 cnt로 뽑아서
        ssum, cnt = q.popleft()

        # 만약 ssum이 M이면 현재까지 cnt를 print하고 함수 종료
        # BFS이므로 먼저 도착했을 때가 최소 연산임!
        if ssum == M:
            print(f'#{tc} {cnt}')
            return

        # 만약 현재 ssum 값이 used에 있지 않으면
        # == BFS는 처음 used에 도착한 값이 최소 연산이므로 이 후에 도착한 값은 최소 연산 X
        if not used[ssum]:

            # 방문 체크 후 문제의 범위 자연수 1000000 이하의 조건을 설정한 뒤
            # 조건에 맞으면 각각 q에 추가하는 형식
            used[ssum] += 1
            if 0 < ssum + 1 <= 1000000:
                q.append((ssum + 1, cnt + 1))
            if 0 < ssum - 1 <= 1000000:
                q.append((ssum - 1, cnt + 1))
            if 0 < ssum * 2 <= 1000000:
                q.append((ssum * 2, cnt + 1))
            if 0 < ssum - 10 <= 1000000:
                q.append((ssum - 10, cnt + 1))

# 인풋
for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    # 최대 사용할 수 있는 값이 1000000이므로 인덱스 범위용 + 1
    used = [0] * 1000001
    # 함수 실행
    check(N)




