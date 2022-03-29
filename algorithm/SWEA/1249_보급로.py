import sys
sys.stdin = open('input.txt')


dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def BFS(x, y):
    global min_v

    queue = [(x, y)]
    while queue:

        r, c = queue.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != -1:
                if visited[nr][nc] == 0:
                    visited[nr][nc] = 1
                    dist[nr][nc] = dist[r][c] + arr[nr][nc]
                    queue.append((nr, nc))
                else:
                    if dist[nr][nc] > dist[r][c] + arr[nr][nc]:
                        dist[nr][nc] = dist[r][c] + arr[nr][nc]
                        queue.append((nr, nc))


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    dist = [[0]*N for _ in range(N)]
    min_v = 100*100*10
    arr[0][0] = -1
    BFS(0, 0)
    print(f'#{tc} {dist[N-1][N-1]}')
