import sys
sys.stdin = open('input (3).txt')

def new_arr(n_arr):
    return [i[:] for i in n_arr]

def counting(arr, n):
    dx = [1, -1, 0]
    dy = [0, 0, 1]
    x = n
    y = 0
    k = 0
    cnt = 0

    while True:
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 100 and 0 <= ny < 100 and arr[ny][nx] == 1:
            arr[ny][nx] = 0
            cnt += 1
            x = nx
            y = ny
            k = 0

        else:
            k = (k + 1) % 3

        if y == 99:
            break

    return cnt

for tc in range(1, 11):
    N = int(input())
    sadari = [list(map(int, input().split())) for _ in range(100)]
    start = []
    for i in range(100):
        if sadari[0][i] == 1:
            start.append(i)
    board = new_arr(sadari)
    min_idx = 0
    min_v = counting(new_arr(sadari), start[0])
    for i in start:
        if counting(new_arr(sadari), i) < min_v:
            min_v = counting(new_arr(sadari), i)
            min_idx = i
    print(f'#{tc} {min_idx}')

