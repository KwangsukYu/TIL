import sys
sys.stdin = open('sample_input.txt')
from itertools import combinations

def max_price(li):
    global ans1, ans2

    comb_res = 0
    for i in range(1, M+1):
        comb = list(combinations(li, i))
        for j in comb:
            res = 0
            if sum(j) <= C:
                for k in j:
                    res += k*k

            if comb_res < res:
                comb_res = res
    return comb_res

def check(visited):
    global ans

    for i in range(N):
        for j in range(N-M+1):
            if j + M - 1 < N:
                for k in  range(M):
                    if visited[i][j+k]:
                        break
                else:
                    tmp2 = max_price(arr[i][j:j+M])
                    if tmp + tmp2 > ans:
                        ans = tmp + tmp2

for tc in range(1, int(input())+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    ans = 0


    for i in range(N):
        for j in range(N-M+1):
            if j + M - 1 < N:
                for k in range(M):
                    visited[i][j + k] = 1
                tmp = max_price(arr[i][j:j+M])
                check(visited)

                for k in range(M):
                    visited[i][j + k] = 0

    print(f'#{tc} {ans}')

