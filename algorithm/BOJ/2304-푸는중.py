def max_n(li):
    max_v = 0
    for i in li:
        if i > max_v:
            max_v = i
    return max_v


space = [0] * 1001
T = int(input())
for ts in range(T):
    x, y = map(int, input().split())
    space[x] = y

ans = 0
first_max = max_n(space)

h = 0
for i in range(len(space)):
    if space[i] == first_max:
        ans += space[i]
        idx = i + 1
        break
    else:
        if space[i] > h:
            h = space[i]
        ans += h
# 오르막길만 있을 때, 내리막길만 있을때 구분해서 풀어보자
for i in range(len(space[idx:])):
    x = max_n(space[idx:])
    ans += x
    if space[idx+i] == x:
        x = max_n(space[idx+i+1:])
        if x == 0:
            break
print(ans)