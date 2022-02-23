M, N = map(int, input().split())

chess_b = ['BW' * 4, 'WB'* 4] * 4   # 비교할 8*8의 체스판
chess_w = ['WB' * 4, 'BW'* 4] * 4   # b,w 시작 케이스 2개를 만들어둠


arr = [input() for _ in range(M)]
min_v = 64

for k in range(M - 8 + 1):         # 8*8씩 비교하면 돌 횟수, 세로
    for l in range(N - 8 + 1):     # 가로
        cnt_w = 0                  # 카운트 초기화 w, b 따로
        cnt_b = 0
        for i in range(8):
            for j in range(8):
                if arr[i+k][j+l] != chess_w[i][j]:  # 8*8 을 돌며 다를경우 카운트 추가
                    cnt_w += 1
                if arr[i+k][j+l] != chess_b[i][j]:
                    cnt_b += 1
        
        if cnt_w < min_v:          # 최소값 비교
            min_v = cnt_w

        if cnt_b < min_v:
            min_v = cnt_b    

print(min_v)
        
                