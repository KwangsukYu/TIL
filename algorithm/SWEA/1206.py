for ts in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 0

    for j in range(2, N-2):
        k = arr[j]
        while k > 0:
            if k > arr[j - 1] and k > arr[j - 2] and k > arr[j + 1] and k > arr[j + 2]:
                result += 1
                k -= 1
            else:
                break
    print(f'#{ts} {result}')