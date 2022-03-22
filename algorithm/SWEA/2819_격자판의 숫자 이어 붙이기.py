import sys
sys.stdin = open('sample_input.txt')

def check(r, c, text):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    if len(text) == 7:
        ans.add(text)
        return

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]

        if 0 <= nr < 4 and 0 <= nc < 4:
            check(nr, nc, text + arr[nr][nc])



for tc in range(1, int(input())+1):
    arr = [input().split() for _ in range(4)]
    ans = set()

    for i in range(4):
        for j in range(4):
            check(i, j, arr[i][j])

    print(f'#{tc} {len(ans)}')