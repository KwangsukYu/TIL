import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for ts in range(1, T + 1):
    K, N, M = map(int, input().split()) # k 최대 이동 수 n 종점 m  충전기 설치 정류장 수
    charger = list(map(int, input().split()))
    arr = [0 for i in range(N + 1)]

    for i in charger:
        arr[i] = 1
    start = 1
    cnt = 0
    restart = 1
    print(arr)

    while True:
        for j in range(start, start + K):
            if arr[j] == 1:
                restart = j + 1
        cnt += 1
        start = restart

        if start + K > N:
            print(f'#{ts} {cnt}')
            break
        if start == N:
            print(f'#{ts} {cnt - 1}')
            break
        if 1 not in arr[start:start + K]:
            print(f'#{ts} {0}')
            break











