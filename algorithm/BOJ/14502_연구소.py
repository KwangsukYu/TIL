# import sys
# sys.setrecursionlimit(10000)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
for i in arr:
    lst += i

visited = [0] * (len(lst))
max_cnt = 0

def make_arr(li):
    new_arr = []
    tmp = []
    for i in range(len(li)):
        tmp.append(li[i])

        if len(tmp) == M:
            new_arr.append(tmp)
            tmp = []
    return new_arr

    
dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

def infection(arr):
    global max_cnt

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                stack = [(i, j)]
                while stack:
                    r, c = stack.pop()
                    
                    if arr[r][c] == 2:
                        for k in range(4):
                            nr = r + dr[k]
                            nc = c + dc[k]
                            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                                arr[nr][nc] = 2
                                stack.append((nr, nc))
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1

    if cnt > max_cnt:
        max_cnt = cnt

def make_safe_area(li, wall, visited):

    if wall <= 0:
        new_arr = make_arr(li)
        infection(new_arr)
        return
    
    for i in range(len(li)):
        if visited[i] == 0 and arr[i//M][i%M] == 0:
            visited[i] = 1
            li[i] = 1
            make_safe_area(li, wall-1, visited)
            li[i] = 0
            visited[i] = 0

make_safe_area(lst, 3, visited)
print(max_cnt)

    

