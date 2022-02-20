def check(num):                         # for문 빠져나오기 편하게 함수로!
    for i in range(C):
        for j in range(R):
            if arr[i][j] == num:
                return j + 1, C - i
    
    return 0

R, C = map(int, input().split())
arr = [[0]*R for _ in range(C)]        # 0으로 된 배열
K = int(input())
dr = [0, 1, 0, -1]                     # 이동 방향이 상 우 하 좌니까 맞춰서 만들어줌
dc = [-1, 0, 1, 0]
k = 0
r = 0
c = C - 1                              # 출발점이 밑부분에서 시작하는 달팽이

for i in range(1, R * C + 1):          # R * C 만큼 돌면서
    arr[c][r] = i                      # 그칸을 i로 만들고 방향을 더해줌
    r += dr[k]
    c += dc[k]

    if r < 0 or c < 0 or r >= R or c >= C or arr[c][r] != 0:  # 만약 인덱스를 벗어나거나 0이 아니면
        r -= dr[k]                     # 다시 빼주고
        c -= dc[k]

        k = (k + 1) % 4                # 방향을 다음 방향으로 바꿔준다

        r += dr[k]                     # 그리고 다시 더해주면 방향 전환
        c += dc[k]

if check(K):
    print(*check(K))                   # 함수에서 x,y좌표를 튜플로 받아서 언팩해줌
else:
    print(0)                           # 아니면 0


    
    