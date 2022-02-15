import sys
sys.stdin = open('sample_input (1).txt')

T = int(input())
for tc in range(1, T+1):
    N, k = map(int, input().split())
    ans = 0
    arr = [i for i in range(1, 13)]
    n = len(arr)

    for i in range(1<<n):
        new_arr = []
        for j in range(n):
            if i & (1<<j):
                new_arr.append(arr[j])
        print(new_arr)

        if len(new_arr) == N and sum(new_arr) == k:
            ans += 1
    print(f'#{tc} {ans}')


