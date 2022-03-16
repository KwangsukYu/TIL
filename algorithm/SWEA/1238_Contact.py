from collections import deque
import sys
sys.stdin = open('input.txt')

def check(s):
    visited[s] = 1
    q.append(s)

    while q:
        s = q.popleft()
        for i in arr[s]:
            if visited[i] == 0:
                visited[i] = visited[s] + 1
                q.append(i)

for tc in range(1, 11):
    D, S = map(int, input().split())
    lst = list(map(int, input().split()))
    arr = [[] for _ in range(D + 1)]
    visited = [0] * (D + 1)
    i = 0
    while True:
        try:
            x, y = lst[i*2], lst[i*2+1]
            arr[x].append(y)
            i += 1
        except:
            break

    q = deque()
    q.append(S)
    visited[S] += 1

    check(S)
    ans = 0
    max_t = max(visited)

    for i in range(len(visited)):
        if visited[i] == max_t:
            if i > ans:
                ans = i

    print(f'#{tc} {ans}')

