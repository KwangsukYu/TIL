from collections import deque

def find_zero(arr):
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0:
                    return True

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

tomato = deque()
zero = 0

if not find_zero(arr):
    print(0)
    exit()

for h in range(H):
    for i in range(N):
        for j in range(M):
            if arr[h][i][j] == 1:
                tomato.append((h, i, j))

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)
dh = (-1, 1)

while tomato:
    h, r, c = tomato.popleft()

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < N and 0 <= nc < M and arr[h][nr][nc] == 0:
            arr[h][nr][nc] = arr[h][r][c] + 1
            tomato.append((h, nr, nc))
    
    for l in range(2):
        nh = h + dh[l]

        if 0 <= nh < H and arr[nh][r][c] == 0:
            arr[nh][r][c] = arr[h][r][c] + 1
            tomato.append((nh, r, c))


if not find_zero(arr):
    max_v = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] > max_v:
                    max_v = arr[h][i][j]
    print(max_v-1)
else:
    print(-1)