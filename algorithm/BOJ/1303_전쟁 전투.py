def BFS(i, j, color):
    global blue, white

    q = [(i, j)]
    arr[i][j] = 0
    cnt = 1
    while q:
        r, c = q.pop(0)

        for dr, dc in ((-1, 0), (1, 0), (0, 1), (0, -1)):
            nr = r + dr
            nc = c + dc

            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == color:
                cnt += 1
                arr[nr][nc] = 0
                q.append((nr, nc))
    
    if color == 'B':
        blue += cnt**2
    else:
        white += cnt**2

C, R = map(int, input().split())
arr = [list(input()) for _ in range(R)]

blue = 0
white = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] != 0:
            BFS(i, j, arr[i][j])

print(white, blue)