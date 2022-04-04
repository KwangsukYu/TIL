import sys
sys.stdin = open('sample_input.txt')

def min_cost(r, used, ssum):
    global ans

    if ssum > ans:
        return

    if r == N:
        if ssum < ans:
            ans = ssum
            return

    for i in range(N):
        if i not in used:
            used.add(i)
            min_cost(r+1, used, ssum + cost[r][i])
            used.remove(i)

for tc in range(1, int(input())+1):
    N = int(input())
    cost = [list(map(int,input().split())) for _ in range(N)]
    used = set()
    ans = 99*15
    min_cost(0, used, 0)
    print(f'#{tc} {ans}')




