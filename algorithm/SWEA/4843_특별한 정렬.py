import sys
sys.stdin = open('sample_input (2).txt')

T = int(input())
for tc in range(1, 2):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N):  # 10개까지 제한하고 밑에다가 최소 최대값을 구한뒤 바꿔주는 방법으로하면 효과적!
        if i % 2:
            for j in range(i, N):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        else:
            for j in range(i, N):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j], arr[i]
        # print(arr)
    print(f'#{tc}', *arr[:10])

