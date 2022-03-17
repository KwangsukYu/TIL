import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def tree(n):
    global cnt

    if n <= N:
        tree(n*2)
        tr[n] = cnt
        cnt += 1
        tree(n*2+1)

for tc in range(1, T + 1):
    N = int(input())
    # 0 4 2 6 1 3 5
    tr = [0] * (N + 1)
    cnt = 1

    tree(1)
    print(f'#{tc} {tr[1]} {tr[N//2]}')

