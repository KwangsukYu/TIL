import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = []
    max_v = 0
    def check(r, c):
        global max_v, ans, t

        sr = r
        sc = c

        stack = []
        stack.append((r, c))

        while stack:
            t += 1
            r, c = stack.pop()

            if t == max_v:
                ans.append(arr[sr][sc])

            if t > max_v:
                max_v = t
                ans = [arr[sr][sc]]

            dr = [0, 0, 1, -1]
            dc = [1, -1, 0, 0]

            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if 0 <= nr < N and 0 <= nc < N and arr[r][c] + 1 == arr[nr][nc]:
                    stack.append((nr, nc))

    for i in range(N):
        for j in range(N):
            t = 0
            check(i, j)


    print(f'#{tc} {min(ans)} {max_v}')