import sys
sys.stdin = open('sample_input.txt')

import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    tr = list(map(int, input().split()))

    # heapq 기본 최소 heap
    h = []

    for i in tr:
        heapq.heappush(h, i)
    print(h)
    # 인덱스 계산 용으로 0을 넣어줌
    h.insert(0, 0)
    c = N
    ans = 0

    # 조상 찾아가면서 ans에 추가해줌
    while c != 0:
        p = c//2
        if h[p]:
            ans += h[p]
        c = p
    print(f'#{tc} {ans}')





