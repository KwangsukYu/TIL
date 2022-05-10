from collections import deque
import sys
input = sys.stdin.readline

# 좌표, 동작 횟수, 말 움직임 횟수
def BFS(sr, sc, cnt, j):
    q = deque()
    q.append((sr, sc, cnt, j))

    while q:
        r, c, cnt, jump = q.popleft()

        # 도착지면 동작 횟수를 리턴해줌
        if r == N - 1 and c == M - 1:
            return cnt

        # 일단 상하좌우로는 무조건 움직일 수 있음
        for dr, dc in monkey:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0' and visited[nr][nc][jump] == 0:
                visited[nr][nc][jump] = 1
                q.append((nr, nc, cnt+1, jump))

        # 아직 말 처럼 움직일 수 있는 횟수가 남았다면...
        if jump < K:
            for dr, dc in horse:
                nr = r + dr
                nc = c + dc

                # 횟수 1 증가시키고 q에 넣어줌
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0' and visited[nr][nc][jump+1] == 0:
                    visited[nr][nc][jump+1] = 1
                    q.append((nr, nc, cnt+1, jump+1))
        
    return -1

K = int(input())
M, N = map(int, input().split())

# 말과 원숭이의 이동 패턴
horse = [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
monkey = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# 3차원 배열 설정 [r][c][jump]
# jump는 말처럼 움직인 횟수
arr = [list(input().split()) for _ in range(N)]
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]


# 시작 지점 설정하고 BFS 시작!
visited[0][0][0] = 1
ans = BFS(0, 0, 0, 0)
print(ans)