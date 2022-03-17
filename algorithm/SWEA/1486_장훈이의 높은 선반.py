import sys

sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    top = list(map(int, input().split()))

    min_v = B
    for i in range(1, 1<<N):
        em = []
        for j in range(N):
            if i & (1<<j):
                em.append(top[j])
        if sum(em) >= B:
            h = sum(em) - B

            if h < min_v:
                min_v = h

    print(f'#{tc} {min_v}')