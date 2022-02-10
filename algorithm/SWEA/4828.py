import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for ts in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    for i in range(N):
        for j in range(i + 1, N):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]

    min_v = a[0]
    max_v = a[-1]
    print(f'#{ts} {max_v - min_v}')



