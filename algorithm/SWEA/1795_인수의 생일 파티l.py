import sys
sys.stdin = open('input.txt')

def dijkstra(s, graph):
    U = [0] * N
    D = [0] * N
    U[s] = 1
    for i in range(N):
        D[i] = graph[s][i]

    for _ in range(1, N):
        min_v = 2<<63-1
        w = 0

        for i in range(N):
            if not U[i] and min_v > D[i]:
                min_v = D[i]
                w = i
        U[w] = 1
        for v in range(N):
            if 0 < graph[w][v] < 2<<63-1:
                D[v] = min(D[v], D[w] + graph[w][v])
    return D

for tc in range(1, 1+int(input())):
    N, M, X = map(int, input().split())
    g = [[2<<63-1] * N for _ in range(N)]
    r_g = [[2 << 63 - 1] * N for _ in range(N)]

    for i in range(M):
        v1, v2, w = map(int, input().split())
        g[v1-1][v2-1] = w
        r_g[v2-1][v1-1] = w
    dist1 = dijkstra(X-1, g)
    dist2 = dijkstra(X-1, r_g)

    max_v = 0

    for i in range(N):
        if i != X-1:
            if dist1[i] + dist2[i] > max_v:
                max_v = dist1[i] + dist2[i]

    print(f'#{tc} {max_v}')

# def Floyd(graph):
#
#     D = [[2<<63-1]*N for _ in range(N)]
#
#     for i in range(N):
#         for j in range(N):
#             D[i][j] = graph[i][j]
#
#     for k in range(N):
#         for i in range(N):
#             for j in range(N):
#                 if D[i][j] > D[i][k] + D[k][j]:
#                     D[i][j] = D[i][k] + D[k][j]
#
#
# for tc in range(1, 1+int(input())):
#     N, M, X = map(int, input().split())
#     g = [[2<<63-1] * N for _ in range(N)]
#     r_g = [[2<<63-1] * N for _ in range(N)]
#     for i in range(M):
#         v1, v2, w = map(int, input().split())
#         g[v1-1][v2-1] = w
#         r_g[v2-1][v1-1] = w

#     dist1 = Floyd(g)
#     dist2 = Floyd(r_g)
#     max_v = 0
#     print(dist1)
#     print(dist2)
#
#     print(max_v)
