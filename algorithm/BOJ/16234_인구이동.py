from collections import deque
import sys

N, L, R = map(int, input().split())


# 연합을 만들고 연합 국가의 좌표를 반환
# 글로벌 변수로 연합 국가의 평균을 할당함
def make_union(r, c):
    global avg

    # 평균값에 계속 좌표값을 더해줌
    avg += arr[r][c]

    # 국가의 좌표를 담을 리스트 설정 후 시작지점 추가
    population = []
    population.append((r, c))

    # 방문체크
    visited[r][c] = 1

    # BFS 탐색 시작
    q = deque()
    q.append((r, c))

    while q:

        # BFS로 4방향 탐색
        r, c = q.popleft()

        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            # 인덱스 범위 안이면서, 인구수 차이가 L이상 R이하이고, 방문하지 않은  곳이면
            if 0 <= nr < N and 0 <= nc < N and L <= abs(arr[nr][nc] - arr[r][c]) <= R and not visited[nr][nc]:

                # 방문체크, 평균에 추가,  Q에 삽입, 국가의 좌표를 population 리스트에 삽입
                visited[nr][nc] = 1
                avg += arr[nr][nc]
                q.append((nr, nc))
                population.append((nr, nc))

    # 모든 반복이 끝나면 총합이 담긴 avg를 리스트의 길이만큼 나눠주면 평균값임
    avg //= len(population)
    return population


    

# 2차원 배열 인풋, 값을 비교할 복사한 배열
arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
new_arr = [i[:] for i in arr]

# 원하는 값은 인구이동이 발생하는 일 수
cnt = 0

# 인구이동이 일어나지 않을 때까지 반복
while True:
    visited = [[0]*N for _ in range(N)]
    avg = 0

    # 모든 좌표를 순회하면서 연합을 만듬
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                a = make_union(i, j)
                if a:
                    # 평균으로 좌표값을 변경
                    for r, c in a:
                        arr[r][c] = avg

            # 초기화 (연합이 한개만 있는 것이 아님!)
            avg = 0

    # 만약 위 과정에서 변동이 없다면 == 인구이동이 일어나지 않는 것, break
    if arr == new_arr:
        break

    # 아니면 복사한 배열을 다시 바뀐 배열로 바꾸고 반복
    else:
        new_arr = [i[:] for i in arr]
    cnt += 1

# 출력
print(cnt)