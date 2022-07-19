for _ in range(int(input())):
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]

    cnt = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '#':
                arr[i][j] = '.'
                q = [(i, j)]

                while q:
                    r, c = q.pop(0)

                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] == '#':
                            arr[nr][nc] = '.'
                            q.append((nr, nc))
                
                cnt += 1
    
    print(cnt)