import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input())+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] for _ in range(N)]
    ans = [[0] for _ in range(N)]
    k_lst = [k*k+(k-1)*(k-1) for k in range(1, 22)]
    max_house = 0
    max_k = N + 1

    def check(r, c, k):
        global max_house

        v = 0
        cnt = 0
        for i in range(N):
            for j in range(N):
                if abs(r - i) + abs(c - j) < k:
                    if arr[i][j] == 1:
                        cnt += 1
                        v += M

        if v - k_lst[k-1] >= 0:
            if max_house < cnt:
                max_house = cnt
            return

    for i in range(N):
        for j in range(N):
            for k in range(1, max_k + 1):
                check(i, j, k)

    print(f'#{tc} {max_house}')



