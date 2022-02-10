import sys
sys.stdin = open('input.txt')

T = int(input())
for ts in range(1, T + 1):
    ans = [0] * 5
    N = [2, 3, 5, 7, 11]
    num = int(input())

    for n in range(len(N)):
        while num % N[n] == 0:
            num = int(num / N[n])
            ans[n] += 1
    print(f'#{ts}', *ans)