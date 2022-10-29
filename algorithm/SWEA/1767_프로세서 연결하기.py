import sys
sys.stdin = open('sample_input.txt')

# 각 코어마다 연결 할 수 있는 방향의 수를 반환하는 함수
def check(r, c):
    cnt = 4
    for dr, dc in ((0, 1), (1, 0), (0, -1), (-1 , 0)):
        for k in range(1, N):
            nr = r + (dr *k); nc = c + (dc * k)
            
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break

            if arr[nr][nc] == 1:
                cnt -= 1
                break
    return cnt

# 좌표와 방향 카운트를 받아서 전선을 연결해주는 함수
def set_line(r, c, res):
    dir = ((-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3))
    for k in range(res[1]):
        nr = r + dir[res[0]][0] * k; nc = c + dir[res[0]][1] * k
        arr[nr][nc] = 2
        

# 코어를 기준으로 연결 할 수 있는 방향 중 최소값을 구한는 함수 res = [방향, 카운트]
def check_line(r, c):
    dir = ((-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3))
    res = [0, N]

    for d in dir:
        cnt = 0
        flag = True
        for k in range(1, N):
            nr = r + (d[0] * k); nc = c + (d[1] * k)

            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                break

            if arr[nr][nc] >= 1:                            # 이 전 동작에서 경로 전선이 이미 깔려있거나 코어가 있는 경우
                flag = False                                # 카운팅 X 
                break

            if not arr[nr][nc]:
                cnt += 1
                if cnt >= res[1]:
                    break

        if cnt < res[1] and flag:                           # 깔 수 있는 방향으로 돌면서 최소값을 갱신
            res[0], res[1] = d[2], cnt
    set_line(r, c, res)                                     # 방향과 최소값으로 원본 배열에 전선 깔기

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    lst = []
    for i in range(1, N-1):
        for j in range(1, N-1):
            if arr[i][j]:
                cnt = check(i, j)
                if cnt:                                         # cnt가 0이면 4방향 모두 연결 할 수 없으므로 조건문 설정
                    lst.append((i, j, cnt))
    
    lst.sort(key= lambda x : x[2])                              # 연결 할 수 있는 방향이 작은 순서로 정렬

    for i in lst:                                               # 연결 할 수 있는 방향을 탐색하면서 최소길이 구하기.
        r = i[0] ; c = i[1]
        check_line(r,c)
    
    ans = 0
    for i in arr:
        cnt = i.count(2)
        ans += cnt
    
    print(f'#{tc} {ans}')