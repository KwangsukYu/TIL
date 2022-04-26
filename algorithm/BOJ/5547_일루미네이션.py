from collections import deque
from pprint import pprint

# A형 문제랑은 다르게 r,c 에서 r 값의 홀짝에 따라 변함
# 맞춰서 짝수일 경우 홀수일 경우로 나눔
even_d = ((-1, -1), (-1, 0), (0, -1), (0, 1), (1, -1), (1, 0))
odd_d = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, 0), (1, 1))

# 인풋을 받는데 0으로 전체 배열을 한 번 더 감싸줌 (== BFS 용)
M, N = map(int, input().split())

arr = [[0] * (M+2)] + [[0] + list(map(int, input().split())) + [0] for _ in range(N)] + [[0] * (M+2)]

# BFS로 바깥의 0부터 시작해서 갈 수 있는 모든 경로를 탐색해서 -1로 변환
# == 건물 밖은 모두 -1
q = deque()
q.append((0, 0))
arr[0][0] = -1
while q:
    r, c = q.popleft()

    if r % 2:
        for dr, dc in odd_d:
            nr = r + dr
            nc = c + dc

            # 인덱스 상하좌우 0을 추가했으니 범위도 +2 씩
            if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 0:
                arr[nr][nc] = -1
                q.append((nr, nc))
    else:
        for dr, dc in even_d:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 0:
                arr[nr][nc] = -1
                q.append((nr, nc))

# 위의 BFS가 완료되면 바깥 부분은 -1, 벽은 1, 안쪽은 0인 상태
# pprint(arr)

# 이제 벽 쪽 외곽을 탐색하는 BFS
# 정답용 cnt와 visited를 인덱스에 맞추어 생성
cnt = 0
visited = [[0] * (M+2) for _ in range(N+2)]

# 각각 순회하면서
for i in range(N+2):
    for j in range(M+2):
        
        # 벽을 찾는 과정
        # 벽인데 아직 방문하지 않았을 경우, 방문 체크하고 BFS시작
        if arr[i][j] == 1 and visited[i][j] == 0:
            q = deque()
            q.append((i, j))
            visited[i][j] = 1

            while q:
                r, c = q.popleft()

                # r이 홀 수 일때 짝수 범위를 돌면서
                if r % 2:
                    for dr, dc in odd_d:
                        nr = r + dr
                        nc = c + dc

                        # 만약 인덱스 범위안에 이어진 벽이있고 방문하지 않았으면 방문체크하고 q에 추가
                        if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))
                        
                        # 외곽 면인 경우는 -1과 맞닿아있으므로 -1일 경우 카운팅
                        elif arr[nr][nc] == -1:
                            cnt += 1
                
                # 짝 수 일때 위와 동일
                else:
                    for dr, dc in even_d:
                        nr = r + dr
                        nc = c + dc

                        if 0 <= nr < N+2 and 0 <= nc < M+2 and arr[nr][nc] == 1 and  visited[nr][nc] == 0:
                            visited[nr][nc] = 1
                            q.append((nr, nc))

                        elif visited[nr][nc] == 0 and arr[nr][nc] == -1:
                            cnt += 1
                

# 결과 출력
print(cnt)
