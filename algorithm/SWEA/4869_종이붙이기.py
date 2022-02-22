import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())//10
    memo = [1, 1]

    for i in range(2, N+1):
        memo.append(memo[i-1] + memo[i-2]*2)

    print(f'#{tc} {memo[-1]}')

















