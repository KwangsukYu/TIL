# 인풋을 받고 배열 외곽에 바다를 추가해줌, 계산하기 편함
N, M = map(int, input().split())
arr = [['.'] * (M+2)] +  [['.'] + list(input()) + ['.'] for _ in range(N)] + [['.'] * (M+2)]

# 다음번에 바다가 될 섬의 좌표를 찾아서 sea에 넣어줌
sea = []
for i in range(N+2):
    for j in range(M+2):
        if arr[i][j] == 'X':
            cnt = 0
            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                ni = i + di
                nj = j + dj

                # 한쪽 면이 바다면 cnt 증가시키고 3이상이면 바다
                if arr[ni][nj] == '.':
                    cnt += 1
                if cnt >= 3:
                    sea.append((i, j))

# 50년 뒤 바다가 될 섬들을 바다로 만들기
for r, c in sea:
    arr[r][c] = '.'

# 지도를 최소로 줄여야하므로 위아래 바다만 있는 경우를 제외
i = 0
while True:
    if arr[i].count('X') == 0:
        arr.pop(i)
    else:
        break

j = len(arr) - 1
while True:
    if arr[j].count('X') == 0:
        arr.pop()
        j -= 1
    else:
        break

# 위 아래 최소값은 윗 부분에서 완성 됨
# 좌 우의 최소값을 구하는 과정
minj = 11
maxj = 0

# 섬이 등장하는 x좌표의 최소값과 최대값을 구하고
for i in range(len(arr)):
    for j in range(M+2):
        if arr[i][j] == 'X':
            if j < minj:
                minj = j
            if j > maxj:
                maxj = j

# 인덱스 슬라이싱으로 출력하기
if arr:
    for i in arr:
        print(''.join(i[minj:maxj+1]))
else:
    print('X')
            