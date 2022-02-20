# R, C = map(int, input().split())
# y, x = map(int, input().split())
# t = int(input())
# k = 0
# r = y
# c = C - x

# dr = [1, -1, -1, -1]
# dc = [-1, -1, 1, -1]
# tm = 0

# while tm < t:
#     tm += 1
#     r += dr[k]              
#     c += dc[k]
    
#     if r < 0 or c < 0 or r > R or c > C:
#         r -= dr[k]
#         c -= dc[k]
#         tm -= 1
#         k = (k + 1) % 4


# print(r, C - c)

W, H = map(int, input().split())
x, y = map(int, input().split())
tm = int(input())
#  x,y 따로 꺾인 횟수를 구해준다! 좌표 + 시간 값 = 전체 이동길이
line_overX = (x + tm) // W ; line_overY = (y + tm) // H
# 꺽인 횟수가 홀수면 전체길이 - 나머지, 짝수면 그냥 나머지가 좌표
fin_x = W - (x + tm) % W if line_overX % 2 else (x + tm) % W
fin_y = H - (y + tm) % H if line_overY % 2 else (y + tm) % H
print(fin_x, fin_y)
