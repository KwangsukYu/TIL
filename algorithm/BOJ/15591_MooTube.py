import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = (map(int, input().split()))
    graph[p].append((q, r))
    graph[q].append((p, r))

for i in range(Q):
    k, v = map(int, input().split())
    visited = [False] * (N + 1)
    visited[v] = True
    ans = 0
    q = [(v, 1000000001)]

    while q:
        v, r = q.pop(0)
        for n_v, n_r in graph[v]:
            n_r = min(r, n_r)
            if n_r >= k and not visited[n_v]:
                ans += 1
                q.append((n_v, n_r))
                visited[n_v] = True
    print(ans)