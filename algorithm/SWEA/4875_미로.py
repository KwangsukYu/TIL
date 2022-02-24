import sys
sys.stdin = open('sample_input.txt')

def DFS(r, c):
    global ans                              # 결과 담을 global 변수
    arr[r][c] = 1                           # 출발지를 1로 만들고
    for i in range(4):                      # 상하좌우를 돌면서
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:     # 인덱스 범위 안에서
            if arr[nr][nc] == 0:            # 0이면
                DFS(nr, nc)                 # 그 위치를 기준으로 다시 DFS함수 호출
            if arr[nr][nc] == 3:            # 만약 3이 도착지면 ans를 1로 만듬
                ans = 1

# def DFS(r, c):
#     global ans
#     if r < 0 or r >= N or c < 0 or c >= N:
#         return
#     if arr[r][c] == 3:
#         ans = 1
#         return
#     if arr[r][c] == 0 or arr[r][c] == 2:
#         arr[r][c] = 1
#         DFS(r - 1, c)
#         DFS(r, c - 1)
#         DFS(r + 1, c)
#         DFS(r, c + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    r = c = 0               # 출발지 초기값
    dr = [0, 0, -1, 1]      # 상하좌우
    dc = [-1, 1, 0, 0]
    ans = 0                 # 결과 값

    for i in range(N):      # 시작 위치 찾아줌
        for j in range(N):
            if arr[i][j] == 2:
                r, c = i, j
                break
    DFS(r, c)              # 시작 위치를 기준으로 DFS함수 호출
    print(f'#{tc} {ans}')



