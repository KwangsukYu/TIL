import sys
sys.stdin = open('sample_input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_zero(v):
    for i in range(len(v)):
        if v[i][2] == 0:
            return True
    else:
        return False

def delete(v):
    while find_zero(v):
        for i in range(len(v)):
            if v[i][2] == 0:
                v.remove(v[i])
                break
    return

def check(v):
    for i in range(len(v)):
        lst = [(v[i][2], v[i][3])]
        for j in range(len(v)):
            if i != j and v[i][0] == v[j][0] and v[i][1] == v[j][1]:
                lst.append((v[j][2], v[j][3]))
                v[j][0] = v[j][1] = v[j][2] = v[j][3] = 0

        if len(lst) > 1:
            max_v = 0
            max_d = 0
            sum_v = 0
            for k in range(len(lst)):
                sum_v += lst[k][0]
                if lst[k][0] > max_v:
                    max_v = lst[k][0]
                    max_d = lst[k][1]
            v[i][2] = sum_v
            v[i][3] = max_d

for tc in range(1, int(input())+1):
    N, M, K = map(int, input().split())
    arr = [[0] for _ in range(N)]
    virus = []

    for i in range(K):
        r, c, n, d = map(int, input().split())
        virus.append([r, c, n, d-1])

    while M > 0:
        for i in virus:
            i[0] += dr[i[3]]
            i[1] += dc[i[3]]

            if i[0] == 0 or i[0] == N - 1 or i[1] == 0 or i[1] == N - 1:
                i[2] //= 2

                if i[3] == 0:
                    i[3] = 1
                elif i[3] == 1:
                    i[3] = 0
                elif i[3] == 2:
                    i[3] = 3
                else:
                    i[3] = 2

        check(virus)
        delete(virus)

        M -= 1

    ans = 0
    for i in range(len(virus)):
        ans += virus[i][2]
    print(f'#{tc} {ans}')
