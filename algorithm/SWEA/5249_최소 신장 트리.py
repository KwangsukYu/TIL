import sys
sys.stdin = open('sample_input.txt')

def prim(r):

    # MST 리스트를 만들고
    MST = [0] * (dest+1)
    MST[r] = 1

    # 총합을 담아 둘 변수
    s = 0

    # 순회는 N - 1
    for _ in range(dest):

        # 최소 정점과 최소값을 갱신할 변수
        u = 0
        min_v = 2<<63-1

        # 모든 정점을 순회
        for i in range(dest+1):

            # 만약 MST에 정점이 있다면
            if MST[i] == 1:

                # 다른 정점 중에 아직 MST에 없고 0 보다 크고 최소값 보다 작은 경우
                for j in range(dest+1):
                    if 0 < g[i][j] < min_v and MST[j] == 0:

                        # 갱신해줌
                        u = j
                        min_v = g[i][j]

        # 총합에 추가하고 MST에 추가해줌
        s += min_v
        MST[u] = 1
        print(MST)

    return s


for tc in range(1, 1+int(input())):
    dest, E = map(int, input().split())
    g = [[0] * (dest+1) for _ in range(dest+1)]

    # MST 조건 무방향, 가중치 그래프
    for i in range(E):
        x, y, w = map(int, input().split())
        g[x][y] = w
        g[y][x] = w
    print(g)
    # prim 알고리즘
    ans = prim(0)
    print(f'#{tc} {ans}')