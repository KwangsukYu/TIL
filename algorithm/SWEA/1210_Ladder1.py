import sys

sys.stdin = open('input (3).txt')

def new_arr(arr):
    board = [i[:] for i in arr]
    return board

def is_goal(n, arr):
    dx = [-1, 1, 0]
    dy = [0, 0, 1]
    x = n
    y = 0
    k = 0

    while True:
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < 100 and 0 <= ny < 100 and arr[ny][nx] >= 1:
            arr[ny][nx] = 0
            x = nx
            y = ny
            k = 0
        else:
            k = (k + 1) % 3
        if y == 98:
            break

    if arr[y + 1][x] == 2:
        return True


for tc in range(1, 11):
    N = int(input())
    sadari = [list(map(int, input().split())) for _ in range(100)]
    num = []

    for i in range(100):
        if sadari[0][i] == 1:
            num.append(i)

    for l in num:
        if is_goal(l, new_arr(sadari)):
            print(f'#{N} {l}')
            break






















