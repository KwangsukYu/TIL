T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tri = [[1] for i in range(N)]   # 가로의 0번째 인덱스는 전부 1이여서 1로 N만큼의 배열을 만듬

    for i in range(1, N):           # 세로 첫째 줄은 1이니까 생략, 다음 줄부터 순회를 돌면서
        for j in range(1, i+1):     # 가로 첫째 줄도 1부터 시작이니 범위를 1부터 돌면서
            if j == i:              # 만약 끝 인덱스면 1을 추가해주고
                tri[i] += [1]
            else:
                tri[i] += [tri[i - 1][j - 1] + tri[i - 1][j]]   # 아니면 위에 줄의 합을 넣어줌
    print(f'#{tc}')
    if N == 1:                      # 1일 경우에는 그냥 1을 출력해주고
        print(*tri[0])
    else:
        for i in tri:               # 나머지는 출력형식에 맞추어 출력!
            print(*i)


