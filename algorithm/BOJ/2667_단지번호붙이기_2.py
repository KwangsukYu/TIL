def BFS(sr, sc):
    q = [(sr, sc)]
    cnt = 1
    while q:
        r, c = q.pop(0)

        for dr, dc in ((0,1),(0,-1),(1,0),(-1,0)):
            nr = r + dr; nc = c + dc

            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                arr[nr][nc] = 0
                cnt += 1
                q.append((nr, nc))
    return cnt
        
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
cnt_list = []

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            arr[i][j] = 0
            cnt = BFS(i, j)
            cnt_list.append(cnt)

print(len(cnt_list))
for i in sorted(cnt_list):
    print(i)
