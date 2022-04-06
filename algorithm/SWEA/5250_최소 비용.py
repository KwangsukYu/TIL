import sys
sys.stdin = open('sample_input.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def BFS(i, j):
    q = [(i, j)]
    dist[i][j] = 0

    while q:
        r, c = q.pop(0)
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < N:

                # 높이가 다른 경우 에너지 추가
                if arr[r][c] < arr[nr][nc]:
                    energy = arr[nr][nc] - arr[r][c]
                    if dist[r][c] + energy + 1 < dist[nr][nc]:
                        dist[nr][nc] =  dist[r][c] + energy + 1
                        q.append((nr, nc))

                # 아니면 그냥 1 더하면서 진행
                else:
                    if dist[r][c] + 1 < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + 1
                        q.append((nr, nc))


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[2<<63-1] * N for _ in range(N)]
    BFS(0, 0)
    print(dist)
    print(f'#{tc} {dist[N-1][N-1]}')


