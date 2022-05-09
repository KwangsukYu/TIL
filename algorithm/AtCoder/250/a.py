H, W = map(int, input().split())
R, C = map(int, input().split())


cnt = 0
for di, dj in ((-1, 0), (1, 0), (0, 1), (0, -1)):
    ni = R-1 + di
    nj = C-1 + dj

    if 0 <= ni < H and 0 <= nj < W:
        cnt += 1

print(cnt)