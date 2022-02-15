# import sys
# sys.stdin = open('input (3).txt')
T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for i in range(N)]
    x, y = 0, 0
    dist = 0

    for i in range(1, N**2 + 1):

        if dist == 0:
            snail[x][y] = i
            x += dx[dist]
            y += dy[dist]

            if x < 0 or y < 0 or x >= N or y >= N or snail[x][y] != 0:
                x -= dx[dist]
                y -= dy[dist]
                dist = 1
                x += dx[dist]
                y += dy[dist]
                continue

        if dist == 1:
            snail[x][y] = i
            x += dx[dist]
            y += dy[dist]

            if x < 0 or y < 0 or x >= N or y >= N or snail[x][y] != 0:
                x -= dx[dist]
                y -= dy[dist]
                dist = 2
                x += dx[dist]
                y += dy[dist]
                continue

        if dist == 2:
            snail[x][y] = i
            x += dx[dist]
            y += dy[dist]

            if x < 0 or y < 0 or x >= N or y >= N or snail[x][y] != 0:
                x -= dx[dist]
                y -= dy[dist]
                dist = 3
                x += dx[dist]
                y += dy[dist]
                continue

        if dist == 3:
            snail[x][y] = i
            x += dx[dist]
            y += dy[dist]

            if x < 0 or y < 0 or x >= N or y >= N or snail[x][y] != 0:
                x -= dx[dist]
                y -= dy[dist]
                dist = 0
                x += dx[dist]
                y += dy[dist]
                continue


    print(f'#{tc}')
    for i in snail:
        print(*i)












