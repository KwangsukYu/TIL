import sys
sys.stdin = open('sample_input.txt')

# 방향 하 좌
dr = (1,0)
dc = (0,1)

def f(r, c, ssum):
    global min_v

    # 만약 도중에 현재 최소값을 넘어가버리면 가지치기
    if ssum >= min_v:
        return

    # 만약 마지막 오른쪽 끝에 도달했을 경우 최소값 갱신
    if r == N-1 and c == N-1:
        if ssum < min_v:
            min_v = ssum

    # 2방향을 순회하면서
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]

        # 인덱스 범위 안이면 ssum에 arr[nr][nc]를 넣어주고 재귀
        if 0 <= nr < N and 0 <= nc < N:
            # ssum += arr[nr][nc]
            f(nr, nc, ssum + arr[nr][nc])
            # ssum -= arr[nr][nc]

# 인풋 받기!
for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    min_v = 13**2*10
    # result = sum(sum(arr, []))
    # 0,0 부터 시작해서 arr[0][0] 값을 f함수에 넣어줌
    f(0, 0, arr[0][0])

    print(f'#{tc} {min_v}')