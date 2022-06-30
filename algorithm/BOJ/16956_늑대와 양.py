R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]

wolves = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'W':
            wolves.append((i, j))


for r, c in wolves:
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nr = r + dr
        nc = c + dc

        if 0 <= nr < R and 0 <= nc < C:
            if arr[nr][nc] == '.':
                arr[nr][nc] = 'D'
            elif arr[nr][nc] == 'S':
                print(0)
                exit()

print(1)
for i in arr:
    print(''.join(i))