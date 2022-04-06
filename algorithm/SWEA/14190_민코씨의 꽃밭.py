import sys
sys.stdin = open('sampleinput.txt.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def BFS(i, j):

    q = [(i, j)]

    while q:
        r, c = q.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 <= nr < N and 0 <= nc < M and new_arr[nr][nc] == 0 and arr[nr][nc] != 0:
                new_arr[nr][nc] = new_arr[r][c] + 1
                bloom[new_arr[nr][nc]] += 1
                if new_arr[nr][nc] + arr[nr][nc] < len(day):
                    day[new_arr[nr][nc] + arr[nr][nc]] -= 1
                q.append((nr, nc))

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    new_arr = [[0]*M for _ in range(N)]
    day = [0] * (N*M)
    bloom = [0] * (N*M)
    sr, sc = map(int, input().split())
    new_arr[sr][sc] = 1
    bloom[1] += 1
    if 1+arr[sr][sc] < len(day):
        day[1+arr[sr][sc]] -= 1
    BFS(sr, sc)

    max_v = 0
    max_idx = 0
    for i in range(1, len(day)):
        bloom[i] += bloom[i-1] + day[i-1]

        if bloom[i]+day[i] > max_v:
            max_v = bloom[i]+day[i]
            max_idx = i

    print(f'#{tc} {max_idx}일 {max_v}개')