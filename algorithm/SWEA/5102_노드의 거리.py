from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

# 인풋 받기
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    lst = [[] for _ in range(51)]
    visited = [0] * 51

    # 정점과 간선정보를 리스트로 받아주기
    for i in range(E):
        x, y = map(int, input().split())
        lst[x].append(y)
        lst[y].append(x)

    # 시작, 목적지 받기
    S, G = map(int, input().split())

    # 시작지를 넣어주고
    queue = deque()
    queue.append(S)

    # 반복문 돌리기
    while queue:
        # 왼쪽 부터 뽑아서
        v = queue.popleft()

        # 뽑은게 도착지면 끝내기
        if v == G:
            break

        # 아니면 lst[v] 방문 할 수 있는 곳 찾아서
        for i in lst[v]:
            # 방문하지 않았으면
            if not visited[i]:
                # 1씩 추가해주기
                visited[i] = visited[v] + 1
                # 다시 넣어주기
                queue.append(i)


    print(f'#{tc} {visited[G]}')