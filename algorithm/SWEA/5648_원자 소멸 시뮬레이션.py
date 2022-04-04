import sys
sys.stdin = open('sample_input.txt')

dr = (0.5, -0.5, 0, 0)
dc = (0, 0, -0.5, 0.5)

def check():
    global ans, oneja

    oneja.sort()
    same = []
    for i in range(len(oneja)-1):
        if oneja[i][0] == oneja[i+1][0] and oneja[i][1] == oneja[i+1][1]:
            if oneja[i] not in same:
                same.append(oneja[i])
            same.append(oneja[i+1])

    for i in same:
        ans += i[3]
        oneja.remove(i)


for tc in range(1, 1+int(input())):
    N = int(input())
    oneja = []
    for _ in range(N):
        c, r, k, e = map(int, input().split())
        oneja.append([r, c, k, e])
    ans = 0
    for _ in range(4004):
        if len(oneja) > 1:
            for i in range(len(oneja)):
                if oneja[i][2] == 0 or oneja[i][2] == 1:
                    oneja[i][0] += dr[oneja[i][2]]
                else:
                    oneja[i][1] += dc[oneja[i][2]]
            check()
        else:
            break

    print(f'#{tc} {ans}')