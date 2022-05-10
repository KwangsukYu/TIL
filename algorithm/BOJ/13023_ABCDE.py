def DFS(s, cnt):

    # 만약 depth가 4면 종료
    if cnt == 4:
        print(1)
        exit()

    # 아니면 추가하고 삭제하는 식으로
    for j in lst[s]:
        if not visited[j]:
            visited[j] += 1
            DFS(j, cnt+1)
            visited[j] = 0

# A - B - C - D - E depth가 4번이면 바로 리턴해주는 형식
N, M = map(int, input().split())
# ans = False
lst = [[] for _ in range(N)]


# 친구관계는 양방향이므로 둘다 받아줌
for i in range(M):
    x, y = map(int, input().split())
    lst[x].append(y)
    lst[y].append(x)

# 각각 DFS를 돌려서 depth가 4가 되는지 확인
for i in range(N):
    visited = [0] * N
    visited[i] += 1
    DFS(i, 0)
else:
    print(0)

