import sys
sys.stdin = open('input (4).txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    arr_c = [[0]*9 for i in range(9)]

    arr_sq = []
    for i in range(9):
        for j in range(9):
            arr_c[i][j] = arr[j][i]

    dx = [-1, 0, 1 , -1, 0, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 0, 1, 1, 1]
    for x, y in [(1, 1), (1, 4), (1, 7), (4, 1), (4, 4), (4, 7), (7, 1), (7, 4), (7, 7)]:
        empty_list = []
        for i in range(9):
            nx = x + dx[i]
            ny = y + dy[i]
            empty_list.append(arr[ny][nx])
        arr_sq.append(empty_list)

    total = arr + arr_c + arr_sq

    for i in total:
        if len(set(i)) != 9:
            print(f'#{tc} {0}')
            break
    else:
        print(f'#{tc} {1}')