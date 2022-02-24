import sys
sys.stdin = open('sample_input.txt')

def f(y):
    global min_v, min_sum, visited

    if min_sum > min_v:
        return

    if y == N:
        if min_sum < min_v:     # 온 길의 합이 min_v 보다 작으면 바꿔줌
            min_v = min_sum

    for i in range(N):
        if visited[i] == 0:    # visited의 [i]번 인덱스가 방문한 곳이 아니면
            visited[i] = 1     # 방문 찍고
            min_sum += arr[y][i]    # min_sum에다가 그 값을 더해줌
            f(y+1)                  # 그리고 밑으로 한칸 이동
            visited[i] = 0          # 다시 재귀 나오면서 방문 한 곳을 다시 미방문으로 해주고
            min_sum -= arr[y][i]    # 다시 합에서 빼줌

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_v = 100         # 자연수 10까지 10줄로
    min_sum = 0
    f(0)
    print(f'#{tc} {min_v}')
