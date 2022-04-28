
# 미완


import sys
from collections import deque

def BFS(lst):
    global ans, K

    q = lst
    while True:
        h = q.popleft()

        if 0 <= h + 1 < 200000001 and visited[h+1] == -1:
            K -= 1
            visited[h+1] = visited[h] + 1
            ans += visited[h+1]
            q.append(h+1)
        
        elif visited[200000000] != -1:
            ad = 1
            ans += visited[200000000] + ad
            ad += 1
            K -= 1
            q.append(2000000002)

        if K == 0:
            return
        
        if 0 <= h - 1 < 200000001 and visited[h-1] == -1:
            K -= 1
            visited[h-1] = visited[h] + 1
            ans += visited[h-1]
            q.append(h-1)

        elif visited[0] != -1:
            ap = 1
            ans += visited[0] + ap
            ap += 1
            K -= 1
            q.append(-1)

        if K == 0:
            return


def switch(num):
    num = int(num) + 100000000
    visited[num] = 0

    return num

N, K = map(int, sys.stdin.readline().rstrip().split())
visited = [-1] * 200000001
sam = deque(map(switch, input().split()))
ans = 0
BFS(sam)

print(ans)
