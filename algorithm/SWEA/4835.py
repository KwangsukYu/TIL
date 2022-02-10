import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for ts in range(1, T + 1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    min_v = 0
    for i in range(M):
        min_v += a[i]
    max_v = 0

    for i in range(N - M + 1):
        x = 0
        y = 0
        for j in range(i, i + M):
            x += a[j]
            y += a[j]

        if max_v < x:
            max_v = x

        if min_v > y:
            min_v = y

    print(f'#{ts} {max_v - min_v}')







