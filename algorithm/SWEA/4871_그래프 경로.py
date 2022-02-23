import sys
sys.stdin = open('sample_input.txt')

def dfs(start, end):
    stack = []
    for i in adjlist[start]:
        stack.append(i)
    while stack:
        v = stack.pop()

        if v == end:
            return 1

        if adjlist[v]:
            for j in adjlist[v]:
                stack.append(j)
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adjlist = [[] for _ in range(V+1)]

    for _ in range(E):
        x, y = map(int,input().split())
        adjlist[x].append(y)

    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S, G)}')
