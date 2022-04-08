# # 상 우 하 좌
# dr = (-1, 0, 1, 0)
# dc = (0, 1, 0, -1)

# # 한 길로만 가면 되니까 DFS
# def DFS(r, c, d):
#     stack = [(r, c, d)]

#     # DFS 템플릿
#     while stack:
#         r, c, d = stack.pop()
        
#         # 정면으로 가는 것이아닌 왼 쪽으로 진행하기 때문에 -1%4를 해줌
#         left = (d - 1)%4
#         nr = r + dr[left]
#         nc = c + dc[left]

#         # 만약 왼 쪽이 청소가 안 되어 있으면
#         if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0':
#             # 청소하고 그 왼쪽 좌표, 왼쪽 방향을 넣어줌
#             arr[nr][nc] = 1
#             stack.append((nr, nc, left))

#         # 만약 청소가 되어있고 벽일 경우엔
#         else:

#             # 2a를 4번 반복해야하므로 cnt 변수 설정 후 4번 순회
#             cnt = 0
#             while cnt < 4:

#                 # cnt가 증가하면서 방향도 달라지니까 d-cnt로 방향 설정
#                 cnt += 1
#                 left = (d - cnt) % 4

#                 nr = r + dr[left]
#                 nc = c + dc[left]
                
#                 # 위 과정과 마찬가지로 왼쪽으로 돌 때마다 청소 유무 확인
#                 # 안 되어있으면 위와 같은 과정 반복 후 1번으로 돌아감
#                 if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '0':
#                     arr[nr][nc] = 1
#                     stack.append((nr, nc, left))
#                     break
                
#                 # 만약 4번을 다 돌았으면
#                 if cnt == 4:

#                     # 뒤는 -2 해주면 됨
#                     back = (d-2) % 4
#                     nr = r + dr[back]
#                     nc = c + dc[back]
                    
#                     # 뒤가 벽이 아니면 후진하고 while문 종료
#                     # 이때 방향은 후진이므로, 처음 들어올 때 방향을 유지
#                     if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '1':
#                         stack.append((nr, nc, d))
#                         break
            
#             # 4번 다 돌고 뒤가 벽이면 return으로 종료
#             else:
#                 return
    
#     # 청소다해도 종료
#     return


# N, M = map(int, input().split())
# r, c, d = map(int, input().split())

# # 행렬은 str 형식으로 받아줌
# arr = [list(input().split()) for _ in range(N)]

# # 첫 위치 int로 초기화 후 DFS 호출
# arr[r][c] = 1
# DFS(r, c, d)

# # DFS가 종료되었으면 int 1의 갯 수를 확인
# cnt = 0
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 1:
#             cnt += 1

# # 출력
# print(cnt)

di = (-1, 0, 1, 0)
dj = (0, 1, 0, -1)

def bfs(si, sj):
    global d

    q = []
    q.append((si,sj))
    v[si][sj] = 1

    while q:
        flag = 0
        ci, cj = q.pop()
        for idx in range(4):
            ni = ci + di[(d-1-idx)%4]
            nj = cj + dj[(d-1-idx)%4]
            if 0<=ni<N and 0<=ni<M and not v[ni][nj] and arr[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1
                d = (d-1-idx)%4
                flag = 1
                break

        if flag == 0:
            ni = ci - di[d]
            nj = cj - dj[d]
            if arr[ni][nj] != 1: # 벽이 아니면
                q.append((ni,nj))
                d = (d-1-idx)%4
            else:
                return

N, M = map(int, input().split())
si, sj, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[0]*M for _ in range(N)]

bfs(si,sj)
print(sum(map(sum,v)))
