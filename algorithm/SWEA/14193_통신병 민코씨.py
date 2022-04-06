import sys
sys.stdin = open('sampleinput.txt')

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def BFS(i, j):
    new_arr = [_[:] for _ in arr]
    q = [(i, j)]
    new_arr[i][j] = 0
    while q:
        r, c = q.pop(0)

        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            if 0 < nr < N and 0 < nc < M:
                if new_arr[nr][nc] == '_':
                    new_arr[nr][nc] = new_arr[r][c] + 1
                    q.append((nr, nc))
                elif new_arr[nr][nc] == 'A' or new_arr[nr][nc] == 'S':
                    idx = node_lst.index((nr, nc))
                    new_arr[nr][nc] = new_arr[r][c] + 1
                    graph[u][idx] = new_arr[r][c] + 1
                    q.append((nr, nc))

def prim(r):
    MST = [0] * L
    MST[r] = 1
    s = 0
    for _ in range(1, L):
        u = 0
        min_v = 2<<63-1

        for i in range(L):
            if MST[i] == 1:
                for j in range(L):
                    if 0 < graph[i][j] < min_v and MST[j] == 0:
                        u = j
                        min_v = graph[i][j]

        s += min_v
        MST[u] = 1
    return s

for tc in range(1, 1+int(input())):
    M, N = map(int, input().split())
    arr = [list(input()) for _ in range(N)]

    node_lst = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'A':
                node_lst.append((i, j))
            elif arr[i][j] == 'S':
                node_lst.append((i, j))
    L = len(node_lst)
    graph = [[0]*L for _ in range(L)]

    for u in range(L):
        r, c = node_lst[u]
        BFS(r, c)
    print(graph)
    ans = prim(0)
    print(f'#{tc} {ans}')

