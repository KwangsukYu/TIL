N = int(input())
s, e = map(int, input().split())
E = int(input())
g = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)

def BFS(s, e):
    q = [s]

    while q:
        v = q.pop(0)

        for i in range(N+1):
            if g[v][i] and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)
                if i == e:
                    print(visited[e]-1)
                    return
    print(-1)
    return
for i in range(E):
    p, c = map(int, input().split())
    g[p][c] = 1
    g[c][p] = 1

visited[s] = 1
BFS(s, e)
