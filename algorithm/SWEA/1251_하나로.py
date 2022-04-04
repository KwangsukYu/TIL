import sys
sys.stdin = open('input.txt')

# 그래프 만들어주는 함수
def make_graph():
    for i in range(N):
        for j in range(N):
            if i != j:
                a = x_v[i] - x_v[j]
                b = y_v[i] - y_v[j]
                g[i][j] = a**2 + b**2

# prim 알고리즘
def prim(r):
    # 정점의 갯수만큼 MST 만들어줌
    MST = [0] * N
    # 방문체크 용 값
    MST[r] = 1
    # 합을 담을 변수
    s = 0

    # 임의의 시작 정점을 제외한 나머지 정점에서 실행
    for _ in range(1, N):
        # 인접한 정점 중 최소 비용을 가지는 정점을 담을 u와 최소값 갱신용 변수
        u = 0
        min_v = 2<<63-1

        # 모든 정점을 순회하면서 == 2차원 배열의 r값
        for i in range(N):
            # MST에 포함되어있는 정점에서
            if MST[i] == 1:
                # 인접한 정점 찾기 == 2차원 배열의 c값
                for j in range(N):

                    # c를 순회하면서 MST에 없고, 0보다 크고 무한대보다 작은 값이 있으면
                    if 0 < g[i][j] < min_v and MST[j] == 0:
                        # 그 정점과 최소값을 갱신 (만약 다른 c값에 더 작은 값이 있으면 그걸로)
                        u = j
                        min_v = g[i][j]

        # 합에 더해주고, MST에 포함시키기
        s += min_v
        MST[u] = 1

        # 0.5를 더해서 버림 = 소수점 1째짜리 반올림
    return int(s*E+0.5)


for tc in range(1, int(input())+1):
    N = int(input())
    x_v = list(map(int, input().split()))
    y_v = list(map(int, input().split()))
    E = float(input())
    g = [[0] * N for _ in range(N)]
    make_graph()
    ans = prim(0)
    print(f'#{tc} {ans}')



