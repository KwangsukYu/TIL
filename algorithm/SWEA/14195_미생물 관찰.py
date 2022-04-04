# import sys
# sys.stdin = open('sampleinput.txt')

# dr = (0, 0, -1, 1)
# dc = (-1, 1, 0, 0)
#
# def BFS(i, j):
#     global A, B, max_v
#     p = arr[i][j]
#     q = [(i, j)]
#     arr[i][j] = '_'
#     cnt = 1
#
#     while q:
#         r, c = q.pop(0)
#
#         for k in range(4):
#             nr = r + dr[k]
#             nc = c + dc[k]
#
#             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == p:
#                 arr[nr][nc] = '_'
#                 q.append((nr, nc))
#                 cnt += 1
#
#     if cnt > max_v:
#         max_v = cnt
#
#     if p == 'A':
#         A += 1
#     else:
#         B += 1
#
#
# for tc in range(1, 1+int(input())):
#     N, M = map(int, input().split())
#     arr = [list(input()) for _ in range(N)]
#     A = B = max_v = 0
#
#     for i in range(N):
#         for j in range(M):
#             if arr[i][j] != '_':
#                 BFS(i, j)
#
#
#     print(f'#{tc} {A} {B} {max_v}')

T = int(input())

def switch(char):
    if char == 'A':
        return 1
    elif char == 'B':
        return 2
    else:
        return 0

def BFS(si, sj, types):
    queue = [(si, sj)]
    cnt = 1

    while queue:
        i, j = queue.pop(0)

        sample[i][j] = 0

        for di, dj in (-1, 0), (0, 1), (1, 0), (0, -1):
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < M and sample[ni][nj] == types:
                sample[ni][nj] = 0
                queue.append((ni, nj))
                cnt += 1

    return cnt, types


for tc in range(1, T+1):
    N, M = map(int, input().split())
    sample = [list(map(switch, input())) for _ in range(N)] # switch: a->1 b->2 _->0

    maxV = 0
    cnt_a = 0
    cnt_b = 0

    for i in range(N):
        for j in range(M):
            if sample[i][j]:
                cnt, types = BFS(i, j, sample[i][j])
                if types == 1:
                    cnt_a += 1
                else:
                    cnt_b += 1
                if maxV < cnt:
                    maxV = cnt
    print(f'#{tc} {cnt_a} {cnt_b} {maxV}')