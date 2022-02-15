import sys
sys.stdin = open('sample_input (2).txt')

def search(page, p_n):
    cnt = 1
    start = 1
    end = page
    while start <= end:
        c = int((start + end)/2)
        if c == p_n:
            return cnt
        elif c < p_n:
            start = c
        else:
            end = c
        cnt += 1

T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    cnt_A = search(P, A)
    cnt_B = search(P, B)

    if cnt_A == cnt_B:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A' if cnt_A < cnt_B else f'#{tc} B')