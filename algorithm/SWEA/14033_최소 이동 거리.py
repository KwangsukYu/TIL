import sys
sys.stdin = open('s_input.txt')

def DFS(s, ssum):
    global min_v

    if ssum > min_v:
        return

    if s == N:
        if ssum < min_v:
            min_v = ssum
            return

    if adjlst[s]: #and not visited[s]:
        for i in range(len(adjlst[s])):
            # visited[s] = 1
            DFS(adjlst[s][i], ssum + dist[s][i])
            # visited[s] = 0


for tc in range(1, 1+int(input())):
    N, E = map(int, input().split())
    adjlst = [[] for _ in range(E+2)]
    # visited = [0 for _ in range(E+2)]
    dist = [[] for _ in range(E+2)]
    min_v = 100000

    for i in range(E):
        s, e, w = map(int, input().split())
        adjlst[s].append(e)
        dist[s].append(w)

    DFS(0, 0)
    print(f'#{tc} {min_v}')