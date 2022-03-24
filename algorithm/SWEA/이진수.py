import sys
sys.stdin = open('sample_input.txt')

# for tc in range(1, int(input())+1):
#     N, T = input().split()
#     print(f'#{tc} {format(int(T, 16), "04b")}')

for tc in range(1, int(input())+1):
    N, T = input().split()
    ans = ''
    for i in range(int(N)):
        ans += format(int(T[i], 16), '04b')
    print(f'#{tc} {ans}')

