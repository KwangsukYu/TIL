from collections import deque
import sys
sys.stdin = open('sample_input.txt')

T  = int(input())

# 인풋 받기
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    q = deque(map(int, input().split()))

    # M번 만큼 왼쪽 꺼내서 오른쪽 넣기
    for _ in range(M):
        q.append(q.popleft())

    print(f'#{tc} {q[0]}')