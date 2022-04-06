dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def BFS(i, j):
    global max_v

    q = [(i, j)]
    cnt = 1
    arr[i][j] = 0
    while q:
        r, c = q.pop()

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
                cnt += 1
                arr[nr][nc] = 0
                q.append((nr, nc))
    
    if cnt > max_v:
        max_v = cnt


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            cnt += 1
            BFS(i, j)
print(cnt)
print(max_v)