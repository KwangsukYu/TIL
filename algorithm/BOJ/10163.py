# N장의 색종이, 1000*1000 범위, x좌표 y 좌표, 너비, 높이

N = int(input())
paper = [[0 for i in range(1001)] for i in range(1001)]
for ts in range(1, N +1):
    x, y, a, b = map(int, input().split())

    for i in range(x, x + a):
        paper[i][y:y+b] = [ts]*b
            
for an in range(1, N+1):
    ans = 0
    for i in paper:
        ans += i.count(an)
    print(ans)
        


