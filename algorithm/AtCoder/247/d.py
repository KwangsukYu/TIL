N = int(input())
ans = []

for i in range(N):
    Q, *order = map(int, input().split())

    if Q == 1:
        ans.append((order[0], order[1]))
    if Q == 2:
        tmp = 0
        while True:
            if ans[0][1] - order[0] >= 0:
                tmp += ans[0][0] * order[0]
                v = ans[0][1] - order[0]
                ans[0] = (ans[0][0], v)
                print(tmp)
                break
            elif ans[0][1] - order[0] < 0:
                tmp += ans[0][0] * ans[0][1]
                order[0] -= ans[0][1]
                ans.pop(0)


