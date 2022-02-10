import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for ts in range(1, T + 1):
    N = int(input())
    num = input()
    arr = [0 for i in range(10)]

    for x in num:
        arr[int(x)] += 1

    set_arr = arr[:]

    for i in range(10):
        for j in range(i + 1, 10):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    print(arr, set_arr)

    for i in range(9, -1, -1):
        if set_arr[i] == arr[-1]:
            print(f'#{ts} {i} {arr[-1]}')
            break

