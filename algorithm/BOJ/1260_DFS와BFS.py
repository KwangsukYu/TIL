def dfs(s, visited1):
    stack = [s]

    while stack:
        v = stack.pop()
        if not visited1[v]:
            visited1[v] = 1
            print(v, end=' ')

            for i in range(V, 0, -1):
                if arr[v][i] and not visited1[i]:
                    stack.append(i)
                    
def bfs(s, visited2):
    queue = [s]

    while queue:
        v = queue.pop(0)
        if not visited2[v]:
            visited2[v] = 1
            print(v, end=' ')

            for i in range(1, V + 1):
                if arr[v][i] and not visited2[i]:
                    queue.append(i)
        
V, E, S = map(int, input().split())
arr = [[0] * (V + 1) for _ in range(V + 1)]
visited1 = [0 for _ in range(V + 1)]
visited2 = visited1[:][:]
order = []

for i in range(E):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1

dfs(S, visited1)
print()
bfs(S, visited2)

