# 100*100 도화지 10*10 색종이
N = int(input())
paper = [[0 for i in range(101)] for i in range(101)]

for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        paper[j][y:y+10] = [1] * 10

ans = 0
for i in paper:
    ans += i.count(1)

print(ans)
