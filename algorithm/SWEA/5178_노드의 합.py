import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    # tr에는 정점의 값을 ch에는 인덱스를 넣어준다.
    tr = [0] * (N + 1)
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)

    # tr에 정점의 값을 input으로 받아서 넣어줌
    for i in range(M):
        x, y = map(int, input().split())
        tr[x] = y

    # ch에 각각 연결된 인덱스 값을 넣어줌 역순으로 돌면서...
    # 2번 인덱스는 4, 5 이런식으로
    for i in range(N, 1, -1):
        if i//2:
            if i % 2:
                ch2[i//2] = i
            else:
                ch1[i//2] = i

    # 후위 순회를 하면 leaf 부분부터 계산하면서 올라오기 때문에
    def post(v):
        if v:
            post(ch1[v])
            post(ch2[v])

            # 만약에 tr[v]에 값이 있고 자식이 존재하면
            if not tr[v] and ch1[v] or ch2[v]:

                # tr[v]에 값을 추가해준다.
                tr[v] = tr[ch1[v]] + tr[ch2[v]]
    post(1)
    print(f'#{tc} {tr[L]}')





