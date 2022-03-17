import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input()); a = round(N**(1/3))
    print(f'#{tc} {a}') if a**3 == N else print(f'#{tc} {-1}')






