R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

cnt = 0
for i in range(R):
    for j in range(C):
        if arr[i][j]:
            q = [(i, j)]
            cnt += 1

            while q:
                r, c = q.pop(0)

                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)):
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < R and 0 <= nc < C and arr[nr][nc]:
                        arr[nr][nc] = 0
                        q.append((nr, nc))

print(cnt)