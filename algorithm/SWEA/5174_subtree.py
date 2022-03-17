import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(E):
        x, y = lst[i*2], lst[i*2+1]
        if not ch1[x]:
            ch1[x] = y
        else:
            ch2[x] = y
    cnt = 0

    def check(N):
        global cnt

        if N:
            # cnt += 1
            check(ch1[N])
            cnt += 1
            check(ch2[N])
            # cnt += 1

    check(N)
    print(f'#{tc} {cnt}')


