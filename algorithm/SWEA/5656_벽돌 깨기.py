from itertools import product

import sys
sys.stdin = open('sample_input.txt')

# 유효 범위 구하기
def in_index(r, c):
    return True if 0 <= r < H and 0 <= c < W else False

# 십자 모양 범위 구하기
def break_range(r, c):
    br = []
    for dr, dc in ((0,1), (0,-1), (1,0), (-1,0)):
        for i in range(1, arr[r][c]):
            nr = r + (dr * i); nc = c + (dc * i)
            if in_index(nr, nc) and arr[nr][nc]:
                br.append((nr, nc))
    return br

# 한칸씩 내려주기
def set_arr():
    for c in range(W):
        i, j = H - 1, H - 2
        while j >= 0:
            if not arr[i][c] and not arr[j][c]:
                j -= 1
            elif not arr[i][c] and arr[j][c]:
                arr[i][c], arr[j][c] = arr[j][c], arr[i][c]
                i -= 1; j -= 1
            elif arr[i][c] and not arr[j][c]:
                i = j; j -= 1
            else:
                i = j-1; j -= 2

# c위치로 떨굴때 벽돌 부수기
def drop_line(c):
    for r in range(H):
        if arr[r][c]:
            break_brick_list = break_range(r,c)
            arr[r][c] = 0

            # 탐색하면서 범위 내에 있으면 계속 break_brick_list에 넣어줌 DFS
            while break_brick_list:
                r, c = break_brick_list.pop()
                tmp = break_range(r, c)
                arr[r][c] = 0
                break_brick_list += tmp
            set_arr()
            return True
    return False
        
T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(H)]

    case = list(product(range(W), repeat=N))

    min_v = 100000000

    # 조합 돌면서 벽돌 부수고 남은 벽돌의 최소값 구함 (== 벽돌을 많이 부순 경우)
    for x in case:
        arr = [i[:] for i in maps]

        for y in x:
            drop_line(y)
        cnt = 0

        for r in range(H):
            if cnt >= min_v:
                break
            for c in range(W):
                if arr[r][c]:
                    cnt += 1
        
        min_v = min(cnt, min_v)
        
        # 0이면 끗
        if not min_v:
            break

    print(f"#{tc} {min_v}")
