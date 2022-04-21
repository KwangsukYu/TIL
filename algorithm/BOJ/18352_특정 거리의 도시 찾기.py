from collections import deque
import sys

V, E, D, S = map(int, sys.stdin.readline().rstrip().split())
adjlst = [[] for _ in range(V+1)]
visited = [0] * (V+1)
dest = []

for _ in range(E):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adjlst[a].append(b)

q = deque()
q.append((S, 0))

while q:
    v, c = q.popleft()

    if c == D:
        if visited[v] == 0:
            visited[v] = 1
            dest.append(v)
            continue

    if visited[v] == 0:
        visited[v] = 1
        for i in adjlst[v]:
            q.append((i, c+1))

if dest:
    dest.sort()
    for i in dest:
        print(i)
else:
    print(-1)