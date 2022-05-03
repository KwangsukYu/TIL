from collections import deque
import sys

# 좌표와 마검의 유무로 BFS 탐색
def BFS(r, c, gram):
    q = deque()
    q.append((r, c, gram))

    while q:
        r, c, gram = q.popleft()

        # 마검이 있을 때 vsitied로 없으면 arr로 방문 체크를 하면서
        # 시간이 오버 되었으면 Fail
        if gram:
            if visited[r][c] > T:
                print('Fail')
                return
        
        else:
            if arr[r][c] > T:
                print('Fail')
                return
                
        # 아니면 마지막 좌표 출력
        if r == N -1 and c == M - 1:
            if gram:
                print(visited[r][c])
                return
            else:
                print(arr[r][c])
                return

        # 마검이 있을 때, 없을때 구분해서 마검이 있으면 visited에 방문체크
        # 없으면 arr에 그대로 방문체크
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M:
                if gram:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] +1
                        q.append((nr, nc, True))

                else:
                    if arr[nr][nc] == '0':
                        arr[nr][nc] = arr[r][c] + 1
                        q.append((nr, nc, False))

                    elif arr[nr][nc] == '2':
                        arr[nr][nc] = arr[r][c] + 1
                        visited[r][c] = arr[r][c]
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc, True))

    print('Fail')
    return

N, M, T = map(int, input().split())
arr = [list(sys.stdin.readline().strip().split()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 시작지점에 마검이 있을 수도?
if arr[0][0] == '2':
    arr[0][0] = 0
    BFS(0, 0, True)

# 아니면 그냥 시작
else:
    arr[0][0] = 0
    BFS(0, 0, False)
