import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    arr = [[0] * 11 for _ in range(11)]
    N = int(input())
    ans = 0
    for tc2 in range(N):
        paper = list(map(int, input().split()))  # x1 y1 x2 y2 color
        for i in range(paper[0], paper[2] + 1):  # x1, x2 + 1
            for j in range(paper[1], paper[3] + 1):  # y1, y2 + 1
                if paper[-1] == 1:
                    if arr[i][j] == 1:
                        continue
                    elif arr[i][j] == 0:
                        arr[i][j] += 1
                    else:
                        arr[i][j] = 3
                        ans += 1
                else:
                    if arr[i][j] == 2:
                        continue
                    elif arr[i][j] == 0:
                        arr[i][j] += 2
                    else:
                        arr[i][j] = 3
                        ans += 1

    print(f'#{tc} {ans}')
